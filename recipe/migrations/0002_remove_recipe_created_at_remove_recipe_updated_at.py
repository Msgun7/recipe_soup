# Generated by Django 4.2.1 on 2023-05-22 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='updated_at',
        ),
    ]