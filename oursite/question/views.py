import os
import sys
import inspect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, OriginInfo

'''
current_dir=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir=os.path.dirname(os.path.dirname(current_dir))
'''
sys.path.insert(0,'../..')
import vacation_id3_attempt_2
from .forms import QuestionForm, OriginInfoForm
import time

# Create your views here.
def question_location(request):
    '''
    The first question asked, namely "Is <location displayed> your current 
    location?". Redirect to different pages based on user response.
    '''

    obj = get_object_or_404(Question, id=1)
    form = QuestionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        if form.cleaned_data['answer'] == 'Y':
            return redirect('../genie/2/')
        else:
            # update the origin info
            return redirect('../origin/')
        form = QuestionForm()
    context = {'form': form, 'object': obj}    
    return render(request, 'questions/get_started.html', context)

def update_origin_info(request):
    obj = get_object_or_404(OriginInfo, id=3)
    form = OriginInfoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = OriginInfoForm()
    context = {'form': form, 'object': obj}
    return render(request, 'origin.html', context)


def question_list_view(request):
    queryset = Question.objects.all()
    context = {'object_list': queryset}
    return render(request, 'questions/question_list.html', context)

REDIRECT_DIC={
        'NATURE_PARKS': 2,
        'TOURS': 3,
        'COLD_OUTDOOR': 4,
        'SIGHTS_AND_LANDMARKS': 5,
        'AMUSEMENT_PARKS': 6,
        'SHOPPING': 7,
        'LAND_OUTDOOR': 8,
        'ZOOS':  9,
        'GROUND_NATURE': 10,
        'CASINOS': 11,
        'OUTDOOR_ACTIVITIES': 12,
        'HISTORIC': 13,
        'SEA_NATURE': 14,
        'SEA_OUTDOOR': 15,
        'CONCERTS_SHOWS': 16,
        'FOOD_DRINK': 17,
        'MUSEUMS': 18
        }

def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Question, id=id)
    form = QuestionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = QuestionForm()
    context = {'object': obj, 'form': form}
    return render(request, 'questions/question_detail.html', context)

def get_answer(request, id):
    obj = get_object_or_404(Question, id=id)
    form = QuestionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return form.cleaned_data['answer']


def update_dictionary(request, column_name, dictionary):
    dictionary[column_name]=int(get_answer(request, REDIRECT_DIC[column_name]))
    return dictionary



def question_location(request):
    '''
    The first question asked, namely "Is <location displayed> your current 
    location?". Redirect to different pages based on user response.
    '''

    obj = get_object_or_404(Question, id=1)
    form = QuestionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        if form.cleaned_data['answer'] == 'Y':
            return redirect('../genie/2/')
        else:
            # update the origin info
            return redirect('../origin/')
        form = QuestionForm()
    context = {'form': form, 'object': obj}    
    return render(request, 'questions/get_started.html', context)

def run_question(request, dictionary, id):
    #return dynamic_lookup_view(request, REDIRECT_DIC[c[1]])
    c=vacation_id3_attempt_2.recurse(0,dictionary)
    if not c[0]:
        return c[1]
    else:
        dynamic_lookup_view(request, REDIRECT_DIC[c[1]])
        time.sleep(5)
        return run_question(request,update_dictionary(request, c[1], dictionary),REDIRECT_DIC[c[1]])



