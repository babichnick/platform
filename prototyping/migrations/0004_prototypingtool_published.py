# Generated by Django 2.1.1 on 2018-09-05 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0003_auto_20180905_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='prototypingtool',
            name='published',
            field=models.BooleanField(default=False, help_text='Tool is visible in the list'),
        ),
    ]
