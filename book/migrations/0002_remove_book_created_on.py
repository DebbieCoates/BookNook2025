# Generated by Django 4.2.17 on 2025-01-13 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='created_on',
        ),
    ]
