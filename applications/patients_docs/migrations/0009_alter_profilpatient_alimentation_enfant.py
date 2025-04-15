# Generated by Django 5.1.7 on 2025-04-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patients_docs", "0008_alter_profilpatient_alimentation_enfant_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profilpatient",
            name="alimentation_enfant",
            field=models.CharField(
                blank=True,
                choices=[("Naturelle", "طبيعية"), ("Artificielle", "اصطناعية")],
                default="Naturelle",
                max_length=200,
                null=True,
                verbose_name="تغدية الطفل",
            ),
        ),
    ]
