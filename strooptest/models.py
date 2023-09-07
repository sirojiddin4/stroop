from django.db import models

class Questionnaire(models.Model):
    # Consent
    consent = models.BooleanField(default=False, verbose_name="I have read the above information and consent to participate in this study.")
    
    # Personal Details
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB', 'Non-Binary'),
        ('NS', 'Prefer not to say'),
    ]
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    EDUCATION_CHOICES = [
        ('HS', 'High School or less'),
        ('SC', 'Some College'),
        ('BD', 'Bachelor\'s Degree'),
        ('MD', 'Master\'s Degree'),
        ('PHD', 'PhD or higher'),
    ]
    education = models.CharField(max_length=3, choices=EDUCATION_CHOICES)

    # Potential Confounding Variables
    sleep_hours = models.IntegerField(choices=[(i, str(i)) for i in range(0, 25)], verbose_name="How many hours of sleep did you get last night?")
    caffeine_consumed = models.BooleanField(verbose_name="Have you consumed any caffeinated beverages today?")
    alcohol_consumed = models.BooleanField(verbose_name="Have you consumed alcohol in the last 24 hours?")
    medication = models.BooleanField(verbose_name="Are you currently taking any medication that affects attention or cognitive function?")
    medication_details = models.TextField(blank=True, verbose_name="If yes, please specify:")
    video_watch_frequency = models.CharField(
        max_length=2,
        choices=[
            ('R', 'Rarely'),
            ('S', 'Sometimes'),
            ('F', 'Frequently'),
            ('V', 'Very frequently'),
        ],
        verbose_name="How often do you watch short videos (less than 1 minute) on platforms like TikTok, Instagram, etc.?"
    )
    stroop_experience = models.BooleanField(verbose_name="Have you ever participated in a Stroop Test before?")
    current_mood = models.CharField(
        max_length=2,
        choices=[
            ('VN', 'Very Negative'),
            ('N', 'Negative'),
            ('NE', 'Neutral'),
            ('P', 'Positive'),
            ('VP', 'Very Positive'),
        ],
        verbose_name="How would you rate your current mood?"
    )

    # Other Information
    email = models.EmailField()

    def __str__(self):
        return self.email

class StroopTest(models.Model):
    user = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=50)
    response_time = models.FloatField()
    is_correct = models.BooleanField()
    word_color_pair = models.CharField(max_length=50)  # New field

