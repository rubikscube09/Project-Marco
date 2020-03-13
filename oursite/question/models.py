from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=10)
    question = models.TextField()
    choices = [(0, 'Not at all'), 
               (1, 'A little bit'), 
               (2, 'Somewhat'), 
               (3, 'Reasonably'), 
               (4, 'Very much'), 
               (5, 'Extremely')]
    answer = models.IntegerField(max_length=1, choices=choices)

    def get_absolute_url(self):
        return reverse('questions:question-list', kwargs={'id': self.id})
    
    def clean_answer(self):
        answer = self.cleaned_data.get('answer')


class OriginInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=20, default='Chicago')
    airport = models.CharField(max_length=10)
    duration = models.IntegerField(default=14)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    num_travelers = models.IntegerField(max_length=1)
    choices = [('Y', 'Yes'), ('N', 'No')]
    answer = models.CharField(max_length=1, choices=choices)

    def clean_answer(self):
        answer = self.clean_data.get('answer')