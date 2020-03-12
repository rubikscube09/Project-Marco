from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, OriginInfo
from .forms import QuestionForm, OriginInfoForm, AltOriginInfoForm, Alt1OriginInfoForm, Alt2OriginInfoForm
from . import vacation_id3_attempt_2
import json
import numpy as np
import pandas as pd
from . import hotels
from . import kiwi
from . import current_location
from . import weather_data

current_loc='chicago'
num_adults=5
#FIND WAY TO ENTER THIS IN USING DJANGO

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

    obj = get_object_or_404(OriginInfo, id=1)
    form = OriginInfoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        if form.cleaned_data['answer'] == 'Y':
            return redirect('../date/')
        else:
            # update the origin info
            return redirect('../origin/')
        form = QuestionForm()
    context = {'form': form, 'object': obj}    
    return render(request, 'questions/get_started.html', context)

def update_origin_info(request):
    obj = get_object_or_404(OriginInfo, id=1)
    form = AltOriginInfoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../date/')
        #form = OriginInfoForm()
    context = {'form': form, 'object': obj}
    return render(request, 'questions/origin.html', context)

def start_date_view(request):
    obj = get_object_or_404(OriginInfo, id=1)
    form = Alt1OriginInfoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../num_travelers/')
        form = Alt1OriginInfoForm()
    context = {'form': form, 'object:': obj}
    return render(request, 'questions/date.html', context)


def num_travelers_view(request):
    obj = get_object_or_404(OriginInfo, id=1)
    form = Alt2OriginInfoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../test/2/')
        #form = Alt2OriginInfoForm()
    context = {'form': form, 'object:': obj}
    return render(request, 'questions/num_travelers.html', context)


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


def get_info(cities_set):
    df=pd.read_csv('question/destinations_with_static_info.csv')
    df=df[df['city'].isin(cities_set)]
    df['hotels']=df.apply(lambda row: hotels.get_hotels(row['trip_advisor_id'], 3, '01/01/2021', 5)[0][0:2], axis=1)
    df['flights']=df.apply(lambda row: kiwi.get_flights('chicago', row['city'], 
                '01/01/21', '01/05/21', 
                roundtrip = True,
                return_from=row['city'], return_to=current_loc, 
                adults=num_adults, children=0, infants=0,
                budget=5000, currency='USD',
                people=0, 
                max_duration=50, 
                radius=50, radius_format= 'km'), axis=1)
    return(df)



def get_cities(request, id):
    global city_set
    global count
    city_set=set([])
    count=0

    def next_question(request, id):
        '''
        Go from one question to another
        How to store the dictionary
        '''
        global city_set
        global count

        with open('result.json', 'r') as f:
            dictionary = json.load(f)
        obj = get_object_or_404(Question, id=id)
        form = QuestionForm(request.POST or None, instance=obj)
        if form.is_valid():
            print(city_set)
            print(count)
            form.save()
            new_qn = run_question(dictionary, id)
            if new_qn in REDIRECT_DIC:
                new_id = REDIRECT_DIC[new_qn]
                return redirect('../../test/{}/'.format(new_id))
            elif len(city_set)>=3 or count>=10:
                context={}
                df=get_info(city_set)
                cities=list(df['city'])
                images=list(df['image'])
                texts=list(df['text'])
                flights=list(df['flights'])
                hotels=list(df['hotels'])
                
                for i in range(len(cities)):
                    city_i='city'+str(i+1)
                    text_i='text'+str(i+1)
                    hotel_costi='hotel_cost'+str(i+1)
                    flight_costi='flight_cost'+str(i+1)
                    image_i='imagelink'+str(i+1)
                    context[city_i]=cities[i].title()
                    context[text_i]=str(texts[i])[1:]
                    context[hotel_costi]=str('We recommend '+hotels[i][0]+' or '+hotels[i][1]+' a night')
                    context[flight_costi]=str(flights[i])
                    context[image_i]='background: url('+str(images[i])[:-3]+');background-size:cover;'
                    
                print(context)
                return render(request, 'questions/result.html', context)
            else:
                city_set.add(new_qn)
                count=count+1
                return next_question(request, id)
        context = {'object': obj, 'form': form}
        return render(request, 'questions/question_detail.html', context)
    return next_question(request, id)
