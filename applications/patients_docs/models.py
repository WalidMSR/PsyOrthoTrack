from django.db import models
from datetime import date
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class ProfilPatient(models.Model):
    choix_genre = [
        ("M", "Homme"),
        ("F", "Femme")
    ]

    @property
    def age_calcule(self):
        today = date.today()
        return today.year - self.date_naissance.year

    prenom = models.CharField("Prénom", max_length=100, blank=True, null=True )
    nom = models.CharField("Nom", max_length=100)
    date_naissance = models.DateField("Date de naissance") 
    lieu_naissance = models.CharField("Lieu de naissance",max_length=50, blank=True, null=True )
 
    genre = models.CharField("Genre", max_length=10, choices=choix_genre)
    adresse = models.CharField("Adresse", max_length=200)

    phone_validator = RegexValidator(r'^\d{10}$', 'Entrez un numéro à 10 chiffres.')
    prenom_pere = models.CharField("Prénom du père", max_length=100, blank=True, null=True)
    numero_telephone_1 = models.CharField("Numéro de téléphone 1", max_length=10, unique=True, validators=[phone_validator])
    prenom_mere = models.CharField("Prénom de la mère", max_length=100, blank=True, null=True)
    numero_telephone_2 = models.CharField("Numéro de téléphone 2", max_length=10, unique=True, blank=True, null=True, validators=[phone_validator])
    
    def clean(self):
        super().clean()
        # Vérifie si le numéro de téléphone 1 existe déjà
        if ProfilPatient.objects.filter(numero_telephone_1=self.numero_telephone_1).exclude(pk=self.pk).exists():
            raise ValidationError({'numero_telephone_1': "Ce numéro de téléphone 1 existe déjà."})

        # Vérifie si le numéro de téléphone 2 existe déjà
        if self.numero_telephone_2 and ProfilPatient.objects.filter(numero_telephone_2=self.numero_telephone_2).exclude(pk=self.pk).exists():
            raise ValidationError({'numero_telephone_2': "Ce numéro de téléphone 2 existe déjà."})
        
    email = models.EmailField("Email", blank=True, null=True)
    photo = models.ImageField("Photo", upload_to="patient_pictures/", blank=True, null=True)

    scolarite = models.CharField("Scolarité", max_length=200, blank=True, null=True)  # Scolarité
    # date_de_rdv = models.DateField("Date d'entretien", default=date.today, blank=True, null=True)  # Date de l'entretien
    
    
    cree_le = models.DateTimeField("Créé le", default=timezone.now, blank=True, null=True)  # Créé le
    type_de_trouble = models.CharField("Type de trouble", max_length=200,blank=True, null=True)  # Type de trouble
    demande = models.TextField("Demande", blank=True, null=True)  # Demande
    envoye_par = models.CharField("Envoyé par", max_length=200, blank=True, null=True)  # Envoyé par

    

    #Informations-dossier médicale
    date_de_creation_dossier = models.DateField("Date du dossier",default=timezone.now, blank=True, null=True)
    description = models.TextField("Description",default="", blank=True, null=True)
    prescription = models.TextField("Prescription",default="", blank=True, null=True)
    
    choix_oui_non = [
        (True, "نعم"),
        (False, "لا")
    ]
    # Maladies ou handicaps
    maladies_ou_handicaps_famille = models.BooleanField("هل توجد امراض أو اعاقات في العائلة ?", choices=choix_oui_non, default=False, blank=True, null=True)
    maladies_ou_handicaps_du_pere = models.BooleanField("من جهة الأب", choices=choix_oui_non, default=False, blank=True, null=True)
    maladies_ou_handicaps_de_la_mere = models.BooleanField("من جهة الام", choices=choix_oui_non, default=False, blank=True, null=True)
    maladies_ou_handicaps_chez_les_freres = models.BooleanField("لدى الأخوم", choices=choix_oui_non, default=False, blank=True, null=True)
    #pas_de_maladies_ou_handicaps = models.BooleanField("لا", choices=choix_oui_non, default=False)

    lien_entre_les_parents = models.CharField("صلة القرابة بين الوالدين", max_length=200, blank=True, null=True)
    nombre_freres_soeurs = models.IntegerField("عدد الأخوة والاخوات", default=0, blank=True, null=True)
    nombre_freres = models.IntegerField("ذكور", default=0, blank=True, null=True)
    nombre_soeurs = models.IntegerField("انات", default=0, blank=True, null=True)

    position_entre_les_freres = models.IntegerField("ترتيبه بين الاخوة", default=0, blank=True, null=True)
    sante_freres_soeurs = models.TextField("صحة الاخوة", blank=True, null=True)

    antecedents_familiaux = models.TextField(" السوابق العائلية", blank=True, null=True)

    VIE_PARENTAL_CHOICES = [
        ('ensemble', 'مع بعض'),
        ('separes', 'منفصلين'),
        ('decedes', 'متوفيان'),
    ]

    vie_parentale = models.CharField("وضعية الوالدين", choices=VIE_PARENTAL_CHOICES, max_length=20, default='ensemble', blank=True, null=True)

    deces_mere = models.BooleanField("وفاة الام", choices=choix_oui_non, default=False, blank=True, null=True)
    deces_pere = models.BooleanField("وفاة الاب", choices=choix_oui_non, default=False, blank=True, null=True)
    deces_parents = models.BooleanField("وفاة الوالدين", choices=choix_oui_non, default=False, blank=True, null=True)

    enfant_vit_avec_les_parents = models.BooleanField("الطفل يعيش مع والديه ", choices=choix_oui_non, default=True, blank=True, null=True)

    composition_familiale = models.TextField("التركيبة الاجتماعية و الثقافية للعائلة", blank=True, null=True)
    profession_pere = models.CharField("مهنة الاب", max_length=200, blank=True, null=True)
    niveau_etudes_pere = models.CharField("مستواه الدراسي", max_length=200, blank=True, null=True)
    profession_mere = models.CharField("مهنة الام", max_length=200, blank=True, null=True)
    niveau_etudes_mere = models.CharField("مستواها الدراسي", max_length=200, blank=True, null=True)
    niveau_economique = models.CharField("المستوى الاقتصادي", max_length=200, blank=True, null=True)
    temps_pour_soins_enfant = models.CharField("الوقت المخصص لرعاية الطفل", max_length=200, blank=True, null=True)

    # Enceinte et accouchement
    grossesse_voulue = models.BooleanField("الحمل مرغوب فيه", choices=choix_oui_non, default=True, blank=True, null=True)
    grossesse_voulue_par_mere = models.BooleanField("من طرف الام", choices=choix_oui_non, default=True, blank=True, null=True)
    grossesse_voulue_par_pere = models.BooleanField("من طرف الاب", choices=choix_oui_non, default=True, blank=True, null=True)
    sexe_voulu = models.BooleanField("الجنس مرغوب فيه", choices=choix_oui_non, default=True, blank=True, null=True)
    grossesse_compromise = models.BooleanField("هل كان الحمل مضطرب", choices=choix_oui_non, default=False, blank=True, null=True)
    type_de_complication = models.CharField("نوع الاضطراب", max_length=200, blank=True, null=True)
    raison_grossesse_compromise = models.TextField("السبب", blank=True, null=True)
    maladies_mere = models.BooleanField("هل اصيبت الام بأمراض", choices=choix_oui_non, default=False, blank=True, null=True)
    prises_medicaments_mere = models.BooleanField("هل تناولت الأدوية", choices=choix_oui_non, default=False, blank=True, null=True)

    # Accouchement
    accouchement_a_terme = models.BooleanField("الولاد في وقتها", choices=choix_oui_non, default=True, blank=True, null=True)
    accouchement_avant_terme = models.BooleanField("الولاد قبل", choices=choix_oui_non, default=False, blank=True, null=True)
    accouchement_apres_terme = models.BooleanField("الولاد بعد", choices=choix_oui_non, default=False, blank=True, null=True)
    type_accouchement = models.CharField("طبيعة الولادة", max_length=50, choices=[('Naturel', 'طبيعية'), ('Césarienne', 'قيصرية')], default="Naturel", blank=True, null=True)

    # Post-accouchement
    sejour_maternite = models.CharField("مدة جلوس الام في المستشفى", max_length=200, blank=True, null=True)
    etat_mere = models.CharField("حالة الام", max_length=200, blank=True, null=True)
    etat_enfant = models.CharField("حالة الطفل", max_length=200, blank=True, null=True)
    cri_de_naissance = models.BooleanField("صرخة الميلاد", choices=choix_oui_non, default=True, blank=True, null=True)
    couleur_enfant = models.CharField("لونه", max_length=200, blank=True, null=True)
    poids_enfant = models.DecimalField("وزنه", max_digits=5, decimal_places=2, blank=True, null=True)
    mis_en_incubateur = models.BooleanField("هل وضع في حاضنة زجاجية", choices=choix_oui_non, default=False, blank=True, null=True)

    alimentation_enfant = models.CharField("تغدية الطفل", max_length=200, choices=[('Naturelle', 'طبيعية'), ('Artificielle', 'اصطناعية')],default="Naturelle", blank=True, null=True)
    alimentation_enfant_duree = models.CharField("المدة", max_length=100, blank=True, null=True)
    sommeil_enfant = models.CharField("نوم الطفل", max_length=200, choices=[('Normal', 'عادي'), ('Perturbé', 'مضطرب')], default="", blank=True, null=True)

    # Développement de l'enfant
    antecedents_maladies_enfant = models.TextField("السوابق المرضية", blank=True, null=True)
    maladies_enfance = models.BooleanField("هل اصيب الطفل بأمراض الطفولة الأولى", choices=choix_oui_non, default=False, blank=True, null=True)
    fievre = models.BooleanField("الحمى", choices=choix_oui_non, default=False, blank=True, null=True)
    jaunisse = models.BooleanField("اليرقان", choices=choix_oui_non, default=False, blank=True, null=True)
    asthme = models.BooleanField("الربو", choices=choix_oui_non, default=False, blank=True, null=True)
    aucune_maladie_enfance = models.BooleanField("لا", choices=choix_oui_non, default=False, blank=True, null=True)

    # Nouveaux champs ajoutés pour les maladies et le développement de l'enfant
    maladies_autres = models.TextField("امراض أخرى", blank=True, null=True)
    
    # Maladies spécifiques
    epilepsie = models.BooleanField("امراض الجهاز العصبي الصرع", choices=choix_oui_non, default=False, blank=True, null=True)
    meningite = models.BooleanField("التهاب السحايا", choices=choix_oui_non, default=False, blank=True, null=True)
    infections_oreilles = models.BooleanField("امراض انف اذن حنجرة التهابات الأذن المتكررة", choices=choix_oui_non, default=False, blank=True, null=True)
    hospitalisation = models.BooleanField("المعالجة في المستشفى", choices=choix_oui_non, default=False, blank=True, null=True)
    age_hospitalisation = models.IntegerField("السن", blank=True, null=True)

    # Développement psycho-moteur
    developpement_psychomoteur = models.TextField("التطور النفسوحركي", blank=True, null=True)
    marche = models.BooleanField("المشي", choices=choix_oui_non, default=False, blank=True, null=True)
    chutes_frequentes = models.BooleanField("السقوط المتكرر", choices=choix_oui_non, default=False, blank=True, null=True)
    sourire_visages_familier = models.BooleanField("الابتسامة للوجوه المألوفة", choices=choix_oui_non, default=False, blank=True, null=True)
    manger_seul = models.BooleanField("الأكل لوحده", choices=choix_oui_non, default=False, blank=True, null=True)
    sasseoir = models.BooleanField("الجلوس", choices=choix_oui_non, default=False, blank=True, null=True)
    main = models.BooleanField("اليد", choices=choix_oui_non, default=False, blank=True, null=True)
    controle_tete = models.BooleanField("التحكم في الرأس", choices=choix_oui_non, default=False, blank=True, null=True)
    ramper = models.BooleanField("الحبو", choices=choix_oui_non, default=False, blank=True, null=True)
    acquisition_proprete = models.BooleanField("سن اكتساب النظافة", choices=choix_oui_non, default=False, blank=True, null=True)
    s_habiller_seul = models.BooleanField("اللباس لوحده", choices=choix_oui_non, default=False, blank=True, null=True)
    
    # Côté sensoriel
    audition = models.BooleanField("السمع", choices=choix_oui_non, default=False, blank=True, null=True)
    vue = models.BooleanField("الرؤية", choices=choix_oui_non, default=False, blank=True, null=True)

    # Développement linguistique
    langage = models.TextField("التطور اللغوي", blank=True, null=True)
    babillage = models.BooleanField("المناغاة", choices=choix_oui_non, default=False, blank=True, null=True)
    utilisation_phonemes = models.BooleanField("استعمال الفونيمات", choices=choix_oui_non, default=False, blank=True, null=True)
    utilisation_mots = models.BooleanField("استعمال الكلمات", choices=choix_oui_non, default=False, blank=True, null=True)
    reponse_mots = models.BooleanField("الاجابة على الاسئلة بكلمة واحدة", choices=choix_oui_non, default=False, blank=True, null=True)
    utilisation_phrase = models.BooleanField("استعمال الكلمة الجملة", choices=choix_oui_non, default=False, blank=True, null=True)
    utilisation_jumelage = models.BooleanField("استعمال الجمل", choices=choix_oui_non, default=False, blank=True, null=True)
    langue_dans_maison = models.CharField("اللغة المستعملة في المنزل", max_length=200, blank=True, null=True)
    langue_enfant_actuelle = models.CharField("لغة الطفل الحالية", max_length=200, blank=True, null=True)

    # Alimentation et déglutition
    alimentation_et_deglutition = models.TextField("الاكل و البلع", blank=True, null=True,default=" ")
    type_alimentation = models.CharField("نوع الاكل", max_length=100, choices=[('Solide', 'صلب'), ('Ecrasé', 'مهروس'), ('Liquide', 'سائل')], default="", blank=True, null=True)
    position_alimentation = models.CharField("الوضعية اثناء الأكل", max_length=200, blank=True, null=True)
    voies_erronnees_alimentation = models.BooleanField("مسارات خاطئة عند الأكل", choices=choix_oui_non, default=False, blank=True, null=True)
    mastication = models.CharField("المضغ", max_length=50, choices=[('Bon', 'جيد'), ('Moyen', 'نوعا ما'), ('Mauvais', 'سيء')], default="", blank=True, null=True)

    # Développement émotionnel et relationnel
    developpement_emotionnel = models.TextField("التطور الوجداني العلائقي", blank=True, null=True)
    relation_freres = models.TextField("علاقة الطفل بإخوته", blank=True, null=True)
    relation_avec_autres = models.TextField("علاقة الطفل مع الآخرين", blank=True, null=True)
    est_social = models.BooleanField("هل هو اجتماعي", choices=choix_oui_non, default=False, blank=True, null=True)
    aime_jouer_avec_autres = models.BooleanField("هل يحب اللعب مع الآخرين", choices=choix_oui_non, default=False, blank=True, null=True)
    enfants_avec_qui_il_joue = models.CharField("الاطفال الذين يحب اللعب معهم", max_length=200, blank=True, null=True)
    
    # Comportement à la maison
    comportement_a_la_maison = models.TextField("سلوك الطفل في البيت", blank=True, null=True)
    sort_seul = models.BooleanField("يخرج لوحده", choices=choix_oui_non, default=False, blank=True, null=True)
    comportement_chez_lui = models.CharField("سلوك الطفل", max_length=200, choices=[('Calme', 'هادئ'), ('Nerveux', 'عصبي'), ('Agité', 'كثير الحركة'), ('Agressif', 'عدواني')], default="", blank=True, null=True)

    # Éducation et scolarité
    scolarite = models.TextField("التمدرس", blank=True, null=True)
    etat_education_prescolaire = models.BooleanField("مرحلة الروضة", default=False, blank=True, null=True)
    retard_scolaire = models.BooleanField("متأخر بالنسبة لسنه", choices=choix_oui_non, default=False, blank=True, null=True)

    # Comportement pendant l'entretien
    comportement_entretien = models.CharField("سلوك الطفل اثناء اجراء المقابلة", max_length=200, choices=[('Calme', 'هادئ'), ('Normal', 'عادي'), ('Très actif', 'كثير الحركة')], default="", blank=True, null=True)

    # Autres observations
    autres_observations = models.TextField("ملاحظات أخرى", blank=True, null=True)

    # Découverte de la maladie
    age_decouverte_maladie = models.IntegerField("سن اكتشاف المرض", blank=True, null=True)
    symptomes_apparents = models.TextField("الاعراض الظاهرة", blank=True, null=True)

    
    class Meta:
        unique_together = ('nom', 'prenom')  # Empêche les doublons exacts
        ordering = ['nom', 'prenom']
        verbose_name = "Documents et ressources"
        verbose_name_plural = "Documents et ressources"
    
    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.date_naissance}"
        
