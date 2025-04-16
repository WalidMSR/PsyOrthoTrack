# Generated by Django 5.1.7 on 2025-04-16 13:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vitrine", "0003_remove_customuser_added_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="added_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
