# Generated by Django 5.1.7 on 2025-04-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patients_docs", "0012_remove_profilpatient_date_de_rdv"),
    ]

    operations = [
        migrations.AddField(
            model_name="profilpatient",
            name="prenom_mere",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Prénom"
            ),
        ),
        migrations.AddField(
            model_name="profilpatient",
            name="prenom_pere",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Prénom"
            ),
        ),
    ]
