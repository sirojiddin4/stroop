from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import QuestionnaireForm, StroopTestForm
from .models import Questionnaire, StroopTest, UserStats
import random
from datetime import datetime
from django.db import IntegrityError

def questionnaire_view(request):
    form = QuestionnaireForm()
    error_message = None
    
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            try:
                
                questionnaire = form.save()
                request.session['user_id'] = questionnaire.id
                request.session['user_email'] = questionnaire.email  # store email in session
                return redirect('instructions_phase1')
            except IntegrityError:
                error_message = "This email has already been used. Please use a different email."

    return render(request, 'stroop/questionnaire.html', {'form': form, 'error_message': error_message})



def instructions_phase1(request):
    return render(request, 'stroop/stroop_instructions_phase_1.html')

def stroop_test_phase1_view(request):
    
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('questionnaire')
    user = Questionnaire.objects.get(id=user_id)

    if 'question_count' not in request.session:
        request.session['question_count'] = 0

    if request.method == "POST":
        selected_color = request.POST.get("response")
        if request.session['task'] == 'C':
            is_correct = (selected_color.upper() == request.session['display_color'])
        else:
            is_correct = (selected_color.upper() == request.session['text'])

        request.session['question_count'] += 1
        if request.session['question_count'] >= 10:
            request.session['question_count'] = 0
            return redirect('instructions_phase2')

    colors = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PURPLE', 'BLACK']
    text = random.choice(colors)
    display_color = random.choice(colors)
    task = random.choice(['C', 'W', 'C', 'W'])

    request.session['text'] = text
    request.session['display_color'] = display_color
    request.session['task'] = task

 

    return render(request, 'stroop/stroop_test_phase1.html', {'text': text, 'display_color': display_color, 'task': task})

def instructions_phase2(request):
    return render(request, 'stroop/stroop_instructions_phase_2.html')

def stroop_test_phase2_view(request):
    
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('questionnaire')

    user = Questionnaire.objects.get(id=user_id)

    if 'question_count' not in request.session:
        request.session['question_count'] = 0

    if 'start_time' not in request.session:
        request.session['start_time'] = datetime.now().timestamp()

    if request.method == "POST":
        
        elapsed_time = datetime.now().timestamp() - request.session['start_time']
        selected_color = request.POST.get("response")
        if request.session['task'] == 'C':
            is_correct = (selected_color.upper() == request.session['display_color'])
        elif request.session['task'] == 'W':
            is_correct = (selected_color.upper() == request.session['text'])

        stroop_test = StroopTest(
            user=user,
            test_type='Phase 2',
            response_time=elapsed_time,
            is_correct=is_correct,
            word_color_pair=f"{request.session.get('text')}_{request.session.get('display_color')}"
        )
        stroop_test.save()

        request.session['question_count'] += 1

        if request.session['question_count'] >= 50:
            request.session['question_count'] = 0
            return redirect('instructions_phase3')
    
    # Generate new values AFTER processing the POST request.
    colors = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PURPLE', 'BLACK']
    text = random.choice(colors)
    display_color = random.choice(colors)
    task = random.choice(['C', 'W'])

    request.session['text'] = text
    request.session['display_color'] = display_color
    request.session['task'] = task
    # Example for phase 1


    return render(request, 'stroop/stroop_test_phase2.html', {'text': text, 'display_color': display_color, 'task': task})

def instructions_phase3(request):
    return render(request, 'stroop/stroop_instructions_phase_3.html')

def stroop_test_phase3_view(request):

    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('questionnaire')

    user = Questionnaire.objects.get(id=user_id)

    if 'question_count' not in request.session:
        request.session['question_count'] = 0

    if 'start_time' not in request.session:
        request.session['start_time'] = datetime.now().timestamp()

    if request.method == "POST":
        elapsed_time = datetime.now().timestamp() - request.session['start_time']
        selected_color = request.POST.get("response")
        if request.session['task'] == 'C':
            is_correct = (selected_color.upper() == request.session['display_color'])
        else:
            is_correct = (selected_color.upper() == request.session['text'])

        stroop_test = StroopTest(
            user=user,
            test_type='Phase 3',
            response_time=elapsed_time,
            is_correct=is_correct,
            word_color_pair=f"{request.session['text']}_{request.session['display_color']}"
        )
        stroop_test.save()

        request.session['question_count'] += 1

        if request.session['question_count'] >= 50:
            request.session['question_count'] = 0
            return redirect('success')

    # Generate new values AFTER processing the POST request.
    colors = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PURPLE', 'BLACK']
    text = random.choice(colors)
    display_color = random.choice(colors)

    request.session['text'] = text
    request.session['display_color'] = display_color

    task = random.choice(['C', 'W', 'C', 'W'])
    request.session['task'] = task


    return render(request, 'stroop/stroop_test_phase3.html', {'text': text, 'display_color': display_color, 'task': task})

def success(request):
    return render(request, 'stroop/success.html')