# Generated by Django 5.0.3 on 2024-05-08 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_division_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='division',
            old_name='logo',
            new_name='logo_uri',
        ),
    ]
