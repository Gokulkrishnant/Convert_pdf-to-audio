# Generated by Django 3.1.2 on 2020-10-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201020_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfaudio',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='recs'),
        ),
    ]
