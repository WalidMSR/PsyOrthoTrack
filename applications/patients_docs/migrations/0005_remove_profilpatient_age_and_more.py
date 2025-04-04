# Generated by Django 5.0 on 2025-04-04 13:50

import datetime
import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patients_docs", "0004_alter_profilpatient_numero_telephone_1_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profilpatient",
            name="age",
        ),
        migrations.RemoveField(
            model_name="profilpatient",
            name="parents_vivent_ensemble",
        ),
        migrations.RemoveField(
            model_name="profilpatient",
            name="parents_vivent_separes",
        ),
        migrations.AddField(
            model_name="profilpatient",
            name="vie_parentale",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ensemble", "مع بعض"),
                    ("separes", "منفصلين"),
                    ("decedes", "متوفيان"),
                ],
                default="ensemble",
                max_length=20,
                null=True,
                verbose_name="وضعية الوالدين",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="accouchement_a_terme",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=True,
                null=True,
                verbose_name="الولاد في وقتها",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="accouchement_apres_terme",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="الولاد بعد",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="accouchement_avant_terme",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="الولاد قبل",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="acquisition_proprete",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="سن اكتساب النظافة",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="aime_jouer_avec_autres",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="هل يحب اللعب مع الآخرين",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="alimentation_enfant",
            field=models.CharField(
                blank=True,
                choices=[("Naturelle", "طبيعية"), ("Artificielle", "اصطناعية")],
                default="Inconnu",
                max_length=200,
                null=True,
                verbose_name="تغدية الطفل",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="asthme",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="الربو",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="aucune_maladie_enfance",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="لا",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="audition",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="السمع",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="babillage",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="المناغاة",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="chutes_frequentes",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="السقوط المتكرر",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="comportement_chez_lui",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Calme", "هادئ"),
                    ("Nerveux", "عصبي"),
                    ("Agité", "كثير الحركة"),
                    ("Agressif", "عدواني"),
                ],
                default="",
                max_length=200,
                null=True,
                verbose_name="سلوك الطفل",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="comportement_entretien",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Calme", "هادئ"),
                    ("Normal", "عادي"),
                    ("Très actif", "كثير الحركة"),
                ],
                default="",
                max_length=200,
                null=True,
                verbose_name="سلوك الطفل اثناء اجراء المقابلة",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="controle_tete",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="التحكم في الرأس",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="cree_le",
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                null=True,
                verbose_name="Créé le",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="cri_de_naissance",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=True,
                null=True,
                verbose_name="صرخة الميلاد",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="date_de_creation_dossier",
            field=models.DateField(
                blank=True,
                default=django.utils.timezone.now,
                null=True,
                verbose_name="Date du dossier",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="date_de_rdv",
            field=models.DateField(
                default=datetime.date.today, verbose_name="Date d'entretien"
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="date_naissance",
            field=models.DateField(verbose_name="Date de naissance"),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="deces_mere",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="وفاة الام",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="deces_parents",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="وفاة الوالدين",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="deces_pere",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="وفاة الاب",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="demande",
            field=models.TextField(blank=True, null=True, verbose_name="Demande"),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="description",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="Description"
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="enfant_vit_avec_les_parents",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=True,
                null=True,
                verbose_name="الطفل يعيش مع والديه ",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="epilepsie",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="امراض الجهاز العصبي الصرع",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="est_social",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="هل هو اجتماعي",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="etat_education_prescolaire",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="مرحلة الروضة"
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="fievre",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="الحمى",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="grossesse_compromise",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="هل كان الحمل مضطرب",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="grossesse_voulue",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=True,
                null=True,
                verbose_name="الحمل مرغوب فيه",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="grossesse_voulue_par_mere",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=True,
                null=True,
                verbose_name="من طرف الام",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="grossesse_voulue_par_pere",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=True,
                null=True,
                verbose_name="من طرف الاب",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="hospitalisation",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="المعالجة في المستشفى",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="infections_oreilles",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="امراض انف اذن حنجرة التهابات الأذن المتكررة",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="jaunisse",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="اليرقان",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="main",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="اليد",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="maladies_enfance",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="هل اصيب الطفل بأمراض الطفولة الأولى",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="maladies_mere",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="هل اصيبت الام بأمراض",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="maladies_ou_handicaps_chez_les_freres",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="لدى الأخوم",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="maladies_ou_handicaps_de_la_mere",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="من جهة الام",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="maladies_ou_handicaps_du_pere",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="من جهة الأب",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="maladies_ou_handicaps_famille",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="هل توجد امراض أو اعاقات في العائلة ?",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="manger_seul",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="الأكل لوحده",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="marche",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="المشي",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="mastication",
            field=models.CharField(
                blank=True,
                choices=[("Bon", "جيد"), ("Moyen", "نوعا ما"), ("Mauvais", "سيء")],
                default="",
                max_length=50,
                null=True,
                verbose_name="المضغ",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="meningite",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="التهاب السحايا",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="mis_en_incubateur",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="هل وضع في حاضنة زجاجية",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="nombre_freres",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="ذكور"
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="nombre_freres_soeurs",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="عدد الأخوة والاخوات"
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="nombre_soeurs",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="انات"
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="numero_telephone_1",
            field=models.CharField(
                max_length=10,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^\\d{10}$", "Entrez un numéro à 10 chiffres."
                    )
                ],
                verbose_name="Numéro de téléphone 1",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="numero_telephone_2",
            field=models.CharField(
                blank=True,
                max_length=10,
                null=True,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^\\d{10}$", "Entrez un numéro à 10 chiffres."
                    )
                ],
                verbose_name="Numéro de téléphone 2",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="position_entre_les_freres",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="ترتيبه بين الاخوة"
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="prescription",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="Prescription"
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="prises_medicaments_mere",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="هل تناولت الأدوية",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="ramper",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="الحبو",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="reponse_mots",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="الاجابة على الاسئلة بكلمة واحدة",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="retard_scolaire",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="متأخر بالنسبة لسنه",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="s_habiller_seul",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="اللباس لوحده",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="sasseoir",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="الجلوس",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="sexe_voulu",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=True,
                null=True,
                verbose_name="الجنس مرغوب فيه",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="sommeil_enfant",
            field=models.CharField(
                blank=True,
                choices=[("Normal", "عادي"), ("Perturbé", "مضطرب")],
                default="",
                max_length=200,
                null=True,
                verbose_name="نوم الطفل",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="sort_seul",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="يخرج لوحده",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="sourire_visages_familier",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="الابتسامة للوجوه المألوفة",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="type_accouchement",
            field=models.CharField(
                blank=True,
                choices=[("Naturel", "طبيعية"), ("Césarienne", "قيصرية")],
                default="Naturel",
                max_length=50,
                null=True,
                verbose_name="طبيعة الولادة",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="type_alimentation",
            field=models.CharField(
                blank=True,
                choices=[("Solide", "صلب"), ("Ecrasé", "مهروس"), ("Liquide", "سائل")],
                default="",
                max_length=100,
                null=True,
                verbose_name="نوع الاكل",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="type_de_trouble",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Type de trouble"
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="utilisation_jumelage",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="استعمال الجمل",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="utilisation_mots",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="استعمال الكلمات",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="utilisation_phonemes",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="استعمال الفونيمات",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="utilisation_phrase",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="استعمال الكلمة الجملة",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="voies_erronnees_alimentation",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="مسارات خاطئة عند الأكل",
            ),
        ),
        migrations.AlterField(
            model_name="profilpatient",
            name="vue",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "نعم"), (False, "لا")],
                default=False,
                null=True,
                verbose_name="الرؤية",
            ),
        ),
    ]
