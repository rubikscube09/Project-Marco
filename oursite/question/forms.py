from django import forms
from .models import Question, OriginInfo

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['answer']
    

class OriginInfoForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget(years=['2020', '2021']))
    class Meta:
        model = OriginInfo
        fields = ['location', 'airport', 'date']