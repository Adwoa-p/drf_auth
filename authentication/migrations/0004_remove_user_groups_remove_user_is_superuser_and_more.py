# Generated by Django 5.1.4 on 2024-12-17 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]
