from django.shortcuts import render

# Create your views here.
def home_view(request):
    my_context = {'title': 'Project Marco',
                  'msg': 'Hello World'}
    return render(request, 'home.html', my_context)

def team_view(request):
    #member1 = {'Abimanyu Choudhary': '(achoudhary@uchicago.edu)'}
    #member2 = {'Ezra Max': '(ezra.d.max@gmail.com)'}
    #member3 = {'Hao Zhu': '(haozhu@uchicago.edu)'}
    #member4 = {'Shiyu Tian': '(shiyutian@uchicago.edu)'}
    team_context = {'team': ['Abimanyu Choudhary (achoudhary@uchicago.edu)', 
                             'Ezra Max (ezra.d.max@gmail.com)',
                             'Hao Zhu (haozhu@uchicago.edu)',
                             'Shiyu Tian (shiyutian@uchicago.edu)' 
                             ]}
    return render(request, 'team.html', team_context)