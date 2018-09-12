# Generated by Django 2.1.1 on 2018-09-12 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0015_auto_20180912_1633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publication',
            options={'get_latest_by': 'pub_date', 'ordering': ('-pub_date',), 'verbose_name_plural': 'Publications'},
        ),
        migrations.RemoveField(
            model_name='tool',
            name='abbreviation',
        ),
        migrations.AddField(
            model_name='tool',
            name='slug',
            field=models.SlugField(default='adobexd', unique=True),
            preserve_default=False,
        ),
    ]