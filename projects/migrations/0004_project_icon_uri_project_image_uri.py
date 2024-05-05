# Generated by Django 5.0.3 on 2024-04-29 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_detailcontributorproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='icon_uri',
            field=models.ImageField(default=1, upload_to='uploads/projects/icons/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='image_uri',
            field=models.ImageField(default=1, upload_to='uploads/projects/thumbnails/'),
            preserve_default=False,
        ),
    ]
