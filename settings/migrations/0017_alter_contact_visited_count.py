# Generated by Django 5.0.3 on 2024-04-05 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0016_alter_contact_created_at_alter_contact_platform_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='visited_count',
            field=models.IntegerField(default=0),
        ),
    ]
