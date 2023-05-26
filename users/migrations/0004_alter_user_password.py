# Generated by Django 4.2.1 on 2023-05-26 12:01

import django.contrib.auth.password_validation
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_nickname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(
                max_length=100,
                validators=[django.contrib.auth.password_validation.validate_password],
            ),
        ),
    ]
