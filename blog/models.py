from django.db import models
from django.utils.translation import gettext_lazy as _ 
from .abstract import BaseModel, OrderModel



class AuthorModel(BaseModel):
    full_name = models.CharField(
        max_length=30, 
        help_text='write full name', 
        verbose_name=_('full name'))
    image = models.ImageField(
        upload_to='blog/authormodel/%Y/%m/%d', 
        help_text='Here you can post a picture of the author',
        verbose_name=_('image'))
    message = models.TextField(
        verbose_name=_('message'), 
        help_text='you leave information about the post')

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "Author"
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")



class BlogPostModel(BaseModel, OrderModel):
    title =  models.CharField(
        max_length=50, 
        help_text='write title', 
        verbose_name=_('title'),)
    description = models.TextField(
        help_text='You write complete information', 
        verbose_name=_('description'))
    author = models.ForeignKey(
        AuthorModel, 
        on_delete=models.CASCADE, 
        related_name='blogpost', 
        verbose_name=_('author'))
    image = models.ImageField(
        upload_to='blog/blogpostmodel/%Y/%m/%d', 
        help_text='you leave a post image')
    comment = models.ForeignKey(
        'CommentModel', 
        on_delete=models.CASCADE,
        related_name='blogpost', 
        verbose_name=_('comment'))
    tags = models.ManyToManyField(
        'TagModel', 
        related_name='blogpost', 
        verbose_name=_('tags'))  
         


    def __str__(self):
        return f"{self.title},{self.description[:50]}"

    class Meta:
        db_table = 'BlogPost'
        verbose_name = _('BlogPost')
        verbose_name_plural = _('BlogPosts')
        ordering = ['order']

class TagModel(models.Model):
    name = models.CharField(max_length=30, 
    help_text='write tagname', 
    verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Tag'
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

class CommentModel(BaseModel):
    name = models.CharField(
        max_length=40, 
        help_text='write your name', 
        verbose_name=_('name'))
    review = models.TextField(
        help_text='write your review', 
        verbose_name=_('review'))
    email = models.EmailField(
        help_text='write your email', 
        verbose_name=_('email'))

    def __str__(self):
        return f"{self.name},{self.email}"

    class Meta:
        db_table = 'Comment'
        verbose_name =_('Comment')
        verbose_name_plural =_('Comments')
        


