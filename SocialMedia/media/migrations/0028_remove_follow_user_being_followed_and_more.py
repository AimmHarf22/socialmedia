# Generated by Django 4.2.6 on 2024-04-07 15:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("media", "0027_alter_user_profile_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="follow",
            name="user_being_followed",
        ),
        migrations.RemoveField(
            model_name="follow",
            name="user_that_is_following",
        ),
        migrations.AddField(
            model_name="follow",
            name="user_being_followed",
            field=models.ManyToManyField(
                null=True, related_name="followers", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="follow",
            name="user_that_is_following",
            field=models.ManyToManyField(
                null=True, related_name="userfollow", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]