# Generated by Django 4.2.4 on 2023-11-01 19:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("solution", "0003_rename_reviws_reviews"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reviews",
            old_name="custmer",
            new_name="customer",
        ),
        migrations.RenameField(
            model_name="reviews",
            old_name="Text",
            new_name="text",
        ),
    ]
