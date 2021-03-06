# Generated by Django 2.1.1 on 2019-01-29 21:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
import prototyping.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('prototyping', '0058_auto_20190127_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=500, unique=True)),
                ('slug', models.SlugField(default='', max_length=200, unique=True)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to=prototyping.models.PathAndRename('linkimage/'))),
                ('url', models.CharField(default='http://', help_text='link to book', max_length=300)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('published', models.BooleanField(default=False, help_text='Book is visible in the list')),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('color', models.CharField(blank=True, help_text='The color which is used to define a category', max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'BookCategories',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prototyping.BookCategory'),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
