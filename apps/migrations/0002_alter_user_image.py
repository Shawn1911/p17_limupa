# Generated by Django 5.0.1 on 2024-01-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(
                default="users/default.jpg", upload_to="users/images"
            ),
        ),
    ]