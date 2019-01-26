# Generated by Django 2.1.1 on 2019-01-26 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0053_auto_20190126_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='currency',
            field=models.IntegerField(choices=[(1, 'USD'), (2, 'EUR'), (3, 'GBP')], default=1),
        ),
    ]
