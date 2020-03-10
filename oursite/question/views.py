from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, OriginInfo
from .forms import QuestionForm, OriginInfoForm
from . import vacation_id3_attempt_2
import json


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
        if form.cleaned_data['answer'] == 0:
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
    return render(request, 'questions/origin.html', context)


def question_list_view(request):
    queryset = Question.objects.all()
    context = {'object_list': queryset}
    return render(request, 'questions/question_list.html', context)


def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Question, id=id)
    form = QuestionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = QuestionForm()
    context = {'object': obj, 'form': form}
    return render(request, 'questions/question_detail.html', context)


def question_list_view(request):
    queryset = Question.objects.all()
    context = {'object_list': queryset}
    return render(request, 'questions/question_list.html', context)


def get_answer(id):
    '''
    Assuming the user has already made an input, get the answer from db.
    '''

    obj = get_object_or_404(Question, id=id)
    return obj.answer


def run_question(dictionary, id):
    '''
    Use the answer to the current question to predict the next best question
    '''

    proceed, qn = vacation_id3_attempt_2.look_for_city(0, dictionary)
    if not proceed:
        return qn
    else:
        dictionary[qn] =  int(get_answer(id))
        # store result into dictionary
        with open('result.json', 'w') as fp:
            json.dump(dictionary, fp)
        # return the next best question to ask
        return qn


def next_question(request, id):
    '''
    Go from one question to another
    How to store the dictionary
    '''

    with open('result.json', 'r') as f:
        dictionary = json.load(f)
    obj = get_object_or_404(Question, id=id)
    form = QuestionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        new_qn = run_question(dictionary, id)
        if new_qn not in REDIRECT_DIC:
            # clear out result.json
            dictionary = {}
            with open('result.json', 'w') as fp:
                json.dump(dictionary, fp)
            result_context = {'place': new_qn}
            return render(request, 'questions/result.html', result_context)
            #return redirect(reverse('questions:result', kwargs={'place': new_qn}))
        new_id = REDIRECT_DIC[new_qn]
        return redirect('../../test/{}/'.format(new_id))
    # next two lines may not be necessary
    context = {'object': obj, 'form': form}
    return render(request, 'questions/question_detail.html', context)
