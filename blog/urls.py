from django.urls import path
from blog.views import PostDetailView, PostView, CommentView


urlpatterns = [
    path("", PostView.as_view(), name='blog'),
    path('<int:pk>/post/', PostDetailView.as_view(), name='blog-single'),
    path('<int:pk>/comment/', CommentView.as_view(), name='comment')
]