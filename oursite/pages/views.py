from django.shortcuts import render
import json

# Create your views here.
def home_view(request):
    # clear json
    dictionary = {}
    with open('result.json', 'w') as fp:
        json.dump(dictionary, fp)
    my_context = {'title': 'Project Marco',
                  'msg': "Life is short, but the world is big"}
    return render(request, 'home.html', my_context)

def team_view(request):
    team_context = {'team': ['Abimanyu Choudhary (achoudhary@uchicago.edu)', 
                             'Ezra Max (ezra.d.max@gmail.com)',
                             'Hao Zhu (haozhu@uchicago.edu)',
                             'Shiyu Tian (shiyutian@uchicago.edu)' 
                             ]}
    return render(request, 'team.html', team_context)