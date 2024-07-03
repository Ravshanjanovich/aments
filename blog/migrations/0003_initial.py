# Generated by Django 5.0.6 on 2024-07-02 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_delete_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(help_text='write full name', max_length=30, verbose_name='full name')),
                ('image', models.ImageField(help_text='Here you can post a picture of the author', upload_to='blog/authormodel/%Y/%m/%d', verbose_name='image')),
                ('message', models.TextField(help_text='you leave information about the post', verbose_name='message')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'db_table': 'Author',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(help_text='write your name', max_length=40, verbose_name='name')),
                ('review', models.TextField(help_text='write your review', verbose_name='review')),
                ('email', models.EmailField(help_text='write your email', max_length=254, verbose_name='email')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='write tagname', max_length=30, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'db_table': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='BlogPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(help_text='write title', max_length=50, verbose_name='title')),
                ('description', models.TextField(help_text='You write complete information', verbose_name='description')),
                ('image', models.ImageField(help_text='you leave a post image', upload_to='blog/blogpostmodel/%Y/%m/%d')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogpost', to='blog.authormodel', verbose_name='author')),
            ],
            options={
                'verbose_name': 'BlogPost',
                'verbose_name_plural': 'BlogPosts',
                'db_table': 'BlogPost',
                'ordering': ['order'],
            },
        ),
    ]
