# Generated by Django 2.1.1 on 2018-09-12 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0014_auto_20180912_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(default='nick', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='tester', unique=True),
            preserve_default=False,
        ),
    ]
