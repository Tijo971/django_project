# Generated by Django 4.1.7 on 2023-06-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webfashion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('colour', models.CharField(blank=True, max_length=20, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
