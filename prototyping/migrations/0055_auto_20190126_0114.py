# Generated by Django 2.1.1 on 2019-01-26 01:14

from django.db import migrations, models
import prototyping.models


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0054_conference_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='header_image',
            field=models.ImageField(default='nologo.jpg', null=True, upload_to=prototyping.models.PathAndRename('conflogo')),
        ),
    ]
