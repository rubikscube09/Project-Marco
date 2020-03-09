from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {'msg': 'Hello World',
                  'from': 'by',
                  'members': ['Abhi', 'Ezra', 'Shiyu', 'Hao']}
    return render(request, 'home.html', my_context)