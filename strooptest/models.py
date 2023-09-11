from django.db import models

class Questionnaire(models.Model):
    # Consent
    consent = models.BooleanField(default=False, verbose_name="I have read the above information and consent to participate in this study. (Men yuqoridagi ma'lumotni o'qib chiqdim va bu tadqiqotda ishtirok etishga rozimanman.)")

    # Personal Details
    age = models.IntegerField(verbose_name="Age (Yoshingiz nechida?)")
    GENDER_CHOICES = [
        ('M', 'Male (Erkak)'),
        ('F', 'Female (Ayol)'),
        ('NB', 'Non-Binary (Noaniq)'),
        ('NS', 'Prefer not to say (Aytishni xohlamayman)'),
    ]
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, verbose_name="Gender (Jinsingiz)")
    EDUCATION_CHOICES = [
        ('HS', 'High School or less (Oliy maktab yoki undan pastroq)'),
        ('SC', 'Some College (Bazi kollej)'),
        ('BD', 'Bachelor\'s Degree (Bakalavr darajasi)'),
        ('MD', 'Master\'s Degree (Magistr darajasi)'),
        ('PHD', 'PhD or higher (PhD yoki undan yuqori)'),
    ]
    education = models.CharField(max_length=3, choices=EDUCATION_CHOICES, verbose_name="Education Level (Ma'lumotingiz)")

    # Potential Confounding Variables
    sleep_hours = models.IntegerField(choices=[(i, str(i)) for i in range(0, 25)], verbose_name="How many hours of sleep did you get last night? (Siz kechqurun nechta soat uxladingiz?)")
    caffeine_consumed = models.BooleanField(verbose_name="Have you consumed any caffeinated beverages today? (Siz bugun kofeinli ichimlik iste'mol qildingizmi?)")
    alcohol_consumed = models.BooleanField(verbose_name="Have you consumed alcohol in the last 24 hours? (Siz oxirgi 24 soatda alkogol iste'mol qildingizmi?)")
    medication = models.BooleanField(verbose_name="Are you currently taking any medication that affects attention or cognitive function? (Siz hozirda diqqat yoki kognitiv funksiyani ta'sir qiladigan dori vositalarini qabul qilyapsizmi?)")
    medication_details = models.TextField(blank=True, verbose_name="If yes, please specify: (Agar ha, iltimos ko'rsating:)")
    video_watch_frequency = models.CharField(
        max_length=2,
        choices=[ ('R', 'Rarely (Kamchilik)'),
            ('S', 'Sometimes (Ba\'zan)'),
            ('F', 'Frequently (Tez-tez)'),
            ('V', 'Very frequently (Juda ko\'p)') ],
        verbose_name="How often do you watch short videos (less than 1 minute) on platforms like TikTok, Instagram, etc.? (Siz TikTok, Instagram kabi platformalarda (1 daqiqadan kamroq) qisqa videolarni qanchalik tez-tez ko'rasiz?)"
    )
    stroop_experience = models.BooleanField(verbose_name="Have you ever participated in a Stroop Test before? (Siz avvalgi Stroop Testida qatnashganmisiz?)")
    current_mood = models.CharField(
        max_length=2,
        choices=[
            ('VN', 'Very Negative (Juda salbiy)'),
            ('N', 'Negative (Salbiy)'),
            ('NE', 'Neutral (Noaniq)'),
            ('P', 'Positive (Ijobiy)'),
            ('VP', 'Very Positive (Juda ijobiy)'),
        ],
        verbose_name="How would you rate your current mood? (Qanday darajada joriy kayfiyatingizga baho berishingiz mumkin?)"
    )

    # Other Information
    email = models.EmailField(verbose_name="Email (Elektron pochta )", unique=True)


    def __str__(self):
        return self.email

class StroopTest(models.Model):
    user = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=50)
    response_time = models.FloatField()
    is_correct = models.BooleanField()
    word_color_pair = models.CharField(max_length=50)  # New field

class UserStats(models.Model):
    user = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    phase = models.CharField(max_length=10)
    avg_accuracy = models.FloatField()
    avg_response_time = models.FloatField()
