# Generated by Django 2.1.1 on 2018-11-11 14:20

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0046_toolbox_header_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toolboxcategory',
            options={'verbose_name_plural': 'ToolboxCategories'},
        ),
        migrations.AlterField(
            model_name='toolbox',
            name='category',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prototyping.Toolboxcategory'),
        ),
        migrations.AlterUniqueTogether(
            name='toolboxcategory',
            unique_together={('parent', 'slug')},
        ),
    ]
