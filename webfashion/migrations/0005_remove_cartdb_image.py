# Generated by Django 4.1.7 on 2023-06-11 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webfashion', '0004_cartdb_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdb',
            name='image',
        ),
    ]
