# Generated by Django 4.2.4 on 2023-11-01 19:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("solution", "0002_reviws"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Reviws",
            new_name="Reviews",
        ),
    ]
