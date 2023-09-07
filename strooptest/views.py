# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import QuestionnaireForm, StroopTestForm
from .models import Questionnaire, StroopTest
import random
from datetime import datetime

def questionnaire_view(request):
    form = QuestionnaireForm()
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            questionnaire = form.save()
            request.session['user_id'] = questionnaire.id  # Store user ID in session
            return redirect('instructions_phase1')  # Redirect to the instructions page for Phase 1
    return render(request, 'stroop/questionnaire.html', {'form': form})

def success(request):
    return render(request, 'stroop/success.html')

def instructions_phase1(request):
    return render(request, 'stroop/stroop_instructions_phase_1.html')


def stroop_test_phase1_view(request):
    if 'question_count' not in request.session:
        request.session['question_count'] = 0
    
    if request.method == "POST":
        request.session['question_count'] += 1
        if request.session['question_count'] >= 10:
            # Reset for the next phases
            request.session['question_count'] = 0
            return redirect('instructions_phase2')

    colors = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PURPLE', 'BLACK']
    text = random.choice(colors)
    display_color = random.choice(colors)
    
    return render(request, 'stroop/stroop_test_phase1.html', {'text': text, 'display_color': display_color})

def instructions_phase2(request):
    return render(request, 'stroop/stroop_instructions_phase_2.html')

def stroop_test_phase2_view(request):
    # Retrieve user ID from session
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('questionnaire')  # Redirect to the questionnaire if user_id is not found

    # Retrieve the Questionnaire object using the user ID
    user = Questionnaire.objects.get(id=user_id)

    if 'question_count' not in request.session:
        request.session['question_count'] = 0

    if 'start_time' not in request.session:
        request.session['start_time'] = datetime.now().timestamp()

    if request.method == "POST":
        elapsed_time = datetime.now().timestamp() - request.session['start_time']
        selected_color = request.POST.get("response")
        is_correct = (selected_color.upper() == request.session['text'])

        # Record details
        stroop_test = StroopTest(
            user=user,  # Use the user fetched from the session
            test_type='Phase 2',
            response_time=elapsed_time,
            is_correct=is_correct,
            word_color_pair=f"{request.session['text']}_{request.session['display_color']}"
        )
        stroop_test.save()

        request.session['question_count'] += 1

        if request.session['question_count'] >= 35:
            request.session['question_count'] = 0
            return redirect('instructions_phase3')

    colors = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PURPLE', 'BLACK']
    text = random.choice(colors)
    display_color = random.choice(colors)

    request.session['text'] = text
    request.session['display_color'] = display_color

    return render(request, 'stroop/stroop_test_phase2.html', {'text': text, 'display_color': display_color})

def instructions_phase3(request):
    return render(request, 'stroop/stroop_instructions_phase_3.html')


def stroop_test_phase3_view(request):
    # Retrieve user ID from session
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('questionnaire')  # Redirect to the questionnaire if user_id is not found

    # Retrieve the Questionnaire object using the user ID
    user = Questionnaire.objects.get(id=user_id)

    if 'question_count' not in request.session:
        request.session['question_count'] = 0

    if 'start_time' not in request.session:
        request.session['start_time'] = datetime.now().timestamp()

    if request.method == "POST":
        elapsed_time = datetime.now().timestamp() - request.session['start_time']
        selected_color = request.POST.get("response")
        is_correct = (selected_color.upper() == request.session['text'])

        # Record details
        stroop_test = StroopTest(
            user=user,  # Use the user fetched from the session
            test_type='Phase 3',
            response_time=elapsed_time,
            is_correct=is_correct,
            word_color_pair=f"{request.session['text']}_{request.session['display_color']}"
        )
        stroop_test.save()

        request.session['question_count'] += 1

        if request.session['question_count'] >= 35:
            request.session['question_count'] = 0
            return redirect('success')  # Redirect to the success page

    colors = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PURPLE', 'BLACK']
    text = random.choice(colors)
    display_color = random.choice(colors)

    request.session['text'] = text
    request.session['display_color'] = display_color

    return render(request, 'stroop/stroop_test_phase3.html', {'text': text, 'display_color': display_color})
