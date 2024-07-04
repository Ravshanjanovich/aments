from django.shortcuts import render, get_object_or_404
from django.db.models.query import  QuerySet
from .models import AuthorModel, BlogPostModel, CommentModel, TagModel
from django.views.generic import  ListView, DetailView, CreateView
from blog.forms import CommentForm
from django.urls import reverse
from django.core.paginator import Paginator



class PostView(ListView):
    template_name = 'blogs/blog.html'
    context_object_name = 'posts'
    paginate_by = 10 


    def get_queryset(self):
        qs = BlogPostModel.objects.order_by("-id")
        tag = self.request.GET.get("tag")
        if tag:
            qs = qs.filter(tag__name=tag)
        return qs

    def get_context_data(self,**kwargs):
        data = super().get_context_data(**kwargs)
        data ['author'] = AuthorModel.objects.all()
        data ['tag'] = TagModel.objects.all()
        return data 


    def blog_list(request):
        posts = BlogPostModel.objects.all()
        return render(request, 'blog/blogpostmodel_list.html', {'posts': posts})

class PostDetailView(DetailView):
    model = BlogPostModel
    template_name = 'blogs/blog-details.html'


class CommentView(CreateView):
    template_name = 'blog-detail.html'
    class_form = CommentForm
    fields = ['name','email',]
    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, pk=self.kwargs.get("pk"))
        return super().form_valid(form)
    def get_success_url(self):
        return reverse("blog:detail", kwargs={'pk':self.kwargs.get("pk")})

    def get_queryset(self):
        return CommentModel.objects.all()