# Generated by Django 2.1.1 on 2018-11-08 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0043_toolboxcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toolbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of app', max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(default='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prototyping.Toolboxcategory')),
            ],
        ),
    ]