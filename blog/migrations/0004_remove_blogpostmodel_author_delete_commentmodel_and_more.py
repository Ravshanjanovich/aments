# Generated by Django 5.0.6 on 2024-07-02 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpostmodel',
            name='author',
        ),
        migrations.DeleteModel(
            name='CommentModel',
        ),
        migrations.DeleteModel(
            name='TagModel',
        ),
        migrations.DeleteModel(
            name='AuthorModel',
        ),
        migrations.DeleteModel(
            name='BlogPostModel',
        ),
    ]
