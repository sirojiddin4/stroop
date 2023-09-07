from django import forms
from .models import Questionnaire, StroopTest

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = '__all__'

class StroopTestForm(forms.ModelForm):
    class Meta:
        model = StroopTest
        fields = ['response_time', 'is_correct']
