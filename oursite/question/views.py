from django.shortcuts import render, get_object_or_404
from .models import Question
from .forms import QuestionForm

# Create your views here.
def question_create_view(request):
    obj = Question.objects.get(id=1)
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = QuestionForm()
    context = {'form': form, 'object': obj}    
    return render(request, 'questions/question_create.html', context)


def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Question, id=id)
    context = {'object': obj}
    return render(request, 'questions/question_detail.html', context)

def question_list_view(request):
    queryset = Question.objects.all()
    context = {'object_list': queryset}
    return render(request, 'questions/question_list.html', context)
