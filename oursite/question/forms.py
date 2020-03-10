from django import forms
from .models import Question, OriginInfo

class QuestionForm(forms.ModelForm):
    CHOICES = [(0, 'Not Interested'), 
               (1, 'A little Interested'), 
               (2, 'Somewhat Interested'), 
               (3, 'Very Interested'), 
               (4, 'Really Interested'), 
               (5, 'Really Very Interested')]
    answer = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    class Meta:
        model = Question
        fields = ['answer']
    

class OriginInfoForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget(years=['2020', '2021']))
    class Meta:
        model = OriginInfo
        fields = ['location', 'airport', 'date']