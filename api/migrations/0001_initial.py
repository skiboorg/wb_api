# Generated by Django 3.1 on 2020-08-24 06:50

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True, verbose_name='Название тега')),
                ('name_slug', models.CharField(blank=True, db_index=True, editable=False, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True, verbose_name='Название статьи')),
                ('name_slug', models.CharField(blank=True, db_index=True, editable=False, max_length=255, null=True)),
                ('image', models.ImageField(null=True, upload_to='post/', verbose_name='Изображение превью 290х140)')),
                ('image_post', models.ImageField(null=True, upload_to='post/', verbose_name='Изображение в шапке статьи 850х500)')),
                ('title', models.CharField(blank=True, max_length=120, null=True, verbose_name='TITLE')),
                ('description', models.TextField(blank=True, null=True, verbose_name='DESCRIPTION')),
                ('short_description', models.TextField(null=True, verbose_name='Короткое описание')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Статья.')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотров')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Отображать статью ?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('tags', models.ManyToManyField(related_name='tags', to='api.Tag', verbose_name='Теги')),
            ],
        ),
    ]