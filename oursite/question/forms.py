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