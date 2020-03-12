from django import forms
from .models import Question, OriginInfo

class QuestionForm(forms.ModelForm):
    CHOICES = [(0, 'Not at all'), 
               (1, 'A little bit'), 
               (2, 'Somewhat'), 
               (3, 'Reasonably'), 
               (4, 'Very much'), 
               (5, 'Extremely')]
    answer = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    class Meta:
        model = Question
        fields = ['answer']
    

class OriginInfoForm(forms.ModelForm):
    CHOICES = [('Y', 'Yes'), ('N', 'No')]
    answer = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    class Meta:
        model = OriginInfo
        fields = ['answer']

class AltOriginInfoForm(forms.ModelForm):
     class Meta:
        model = OriginInfo
        fields = ['location']

class Alt1OriginInfoForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget(years=['2020','2021']))
    class Meta:
        model = OriginInfo
        fields = ['date']

class Alt2OriginInfoForm(forms.ModelForm):
    class Meta:
        model = OriginInfo
        fields = ['num_travelers']