# Generated by Django 5.0.1 on 2024-04-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photography',
            name='img_photo',
            field=models.ImageField(blank=True, upload_to='Photography/img'),
        ),
    ]
