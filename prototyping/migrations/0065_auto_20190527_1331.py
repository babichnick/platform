# Generated by Django 2.1.1 on 2019-05-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0064_auto_20190513_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='content',
            field=models.TextField(default='', max_length=40000),
        ),
    ]
