# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.questionnaire_view, name='questionnaire'),
    path('instructions_phase1/', views.instructions_phase1, name='instructions_phase1'),
    path('stroop_test_phase1/', views.stroop_test_phase1_view, name='stroop_test_phase1'),
    path('instructions_phase2/', views.instructions_phase2, name='instructions_phase2'),
    path('stroop_test_phase2/', views.stroop_test_phase2_view, name='stroop_test_phase2'),
    path('instructions_phase3/', views.instructions_phase3, name='instructions_phase3'),
    path('stroop_test_phase3/', views.stroop_test_phase3_view, name='stroop_test_phase3'),
    path('success/', views.success, name='success'),
]
