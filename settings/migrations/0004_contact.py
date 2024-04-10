# Generated by Django 5.0.3 on 2024-03-30 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_setting_logo_uri'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('platform', models.CharField(max_length=255, null=True)),
                ('icon_uri', models.ImageField(upload_to='uploads/contact/')),
                ('value', models.CharField(max_length=255, null=True)),
                ('visited_count', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]