# Generated by Django 4.2.6 on 2024-03-03 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("media", "0009_rename_follower_follow_one_being_followed_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="follow",
            old_name="one_being_followed",
            new_name="user_being_followed",
        ),
        migrations.RenameField(
            model_name="follow",
            old_name="one_that_is_following",
            new_name="user_that_is_following",
        ),
    ]
