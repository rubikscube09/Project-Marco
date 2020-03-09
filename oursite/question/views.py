from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, OriginInfo
from .forms import QuestionForm, OriginInfoForm

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