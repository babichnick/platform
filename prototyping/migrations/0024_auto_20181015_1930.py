# Generated by Django 2.1.1 on 2018-10-15 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0023_prototypingtool_voice'),
    ]

    operations = [
        migrations.AddField(
            model_name='prototypingtool',
            name='import_from_dropbox',
            field=models.BooleanField(default=False, help_text='Import from Dropbox'),
        ),
        migrations.AddField(
            model_name='prototypingtool',
            name='import_from_mobile_camera',
            field=models.BooleanField(default=False, help_text='Import from Mobile Camera'),
        ),
        migrations.AddField(
            model_name='prototypingtool',
            name='import_from_photoshop',
            field=models.BooleanField(default=False, help_text='Import from Adobe Photoshop'),
        ),
        migrations.AddField(
            model_name='prototypingtool',
            name='import_from_sketch',
            field=models.BooleanField(default=False, help_text='Import from Sketch'),
        ),
    ]