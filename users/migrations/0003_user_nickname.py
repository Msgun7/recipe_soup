# Generated by Django 4.2.1 on 2023-05-26 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="nickname",
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]