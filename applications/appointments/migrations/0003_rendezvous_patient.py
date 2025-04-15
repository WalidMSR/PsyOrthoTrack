# Generated by Django 5.1.7 on 2025-04-14 21:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointments", "0002_alter_rendezvous_options_and_more"),
        ("patients_docs", "0014_alter_profilpatient_prenom_mere_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="rendezvous",
            name="patient",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="patients_docs.profilpatient",
            ),
        ),
    ]
