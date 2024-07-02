from django.db import models
from django.utils.translation import gettext_lazy as _ 
from .abstract import BaseModel



class AuthorModel(BaseModel):
    full_name = models.CharFiled(
        max_length=30, 
        help_text='write full name', 
        verbose_name=_('full name'))
    image = models.ImageField(
        upload_to='blog/authormodel/%Y/%m/%d', 
        help_text='Here you can post a picture of the author',
        verbose_name=_('image'))

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "Author"
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

