# Generated by Django 5.0.1 on 2024-01-13 10:46

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0002_alter_user_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=django_resized.forms.ResizedImageField(
                crop=["middle", "center"],
                default="users/default.jpg",
                force_format="JPEG",
                keep_meta=True,
                quality=75,
                scale=0.5,
                size=[200, 200],
                upload_to="users/images",
            ),
        ),
    ]
