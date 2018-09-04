# Generated by Django 2.1.1 on 2018-09-04 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prototypingtool',
            name='cost_purchase',
            field=models.PositiveSmallIntegerField(default=1987),
        ),
        migrations.AddField(
            model_name='prototypingtool',
            name='cost_subscription',
            field=models.PositiveSmallIntegerField(default=1987),
        ),
        migrations.AddField(
            model_name='prototypingtool',
            name='last_updated',
            field=models.DateField(default='1987-06-03'),
        ),
    ]
