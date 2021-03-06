# Generated by Django 2.1.1 on 2018-09-09 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0011_publication_tool'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='headline',
        ),
        migrations.AddField(
            model_name='publication',
            name='content',
            field=models.TextField(default='', max_length=8000),
        ),
        migrations.AddField(
            model_name='publication',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='publication',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='tool',
            name='abbreviation',
            field=models.CharField(default='', help_text='Abbreviation of the app', max_length=50, unique=True),
        ),
    ]
