# Generated by Django 5.0.3 on 2024-05-09 18:03

import common.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_visited_count_alter_news_media_uri'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailnewsmedia',
            name='description',
        ),
        migrations.RemoveField(
            model_name='detailnewsmedia',
            name='title',
        ),
        migrations.AlterField(
            model_name='detailnewsmedia',
            name='media_uri',
            field=models.ImageField(null=True, upload_to='uploads/news/media/', validators=[common.validators.validate_image_size]),
        ),
        migrations.AlterField(
            model_name='detailnewsmedia',
            name='news_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news'),
        ),
    ]
