# Generated by Django 2.1.1 on 2018-10-11 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0019_auto_20181011_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='cons',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='tool',
            name='pros',
            field=models.TextField(default=''),
        ),
    ]