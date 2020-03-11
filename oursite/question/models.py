from django.db import models
from django.urls import reverse

# Create your models here.
class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=10)
    question = models.TextField()
    choices = [(0, 'Not Interested'), 
               (1, 'A little Interested'), 
               (2, 'Somewhat Interested'), 
               (3, 'Very Interested'), 
               (4, 'Really Interested'), 
               (5, 'Really Very Interested')]
    answer = models.IntegerField(max_length=1, choices=choices)

    def get_absolute_url(self):
        return reverse('questions:question-list', kwargs={'id': self.id})
    
    def clean_answer(self):
        answer = self.cleaned_data.get('answer')


class OriginInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=20)
    airport = models.CharField(max_length=10)
    date = models.DateField()
    num_travelers = models.IntegerField(max_length=1)
    choices = [('Y', 'Yes'), ('N', 'No')]
    answer = models.CharField(max_length=1, choices=choices)

    def clean_answer(self):
        answer = self.clean_data.get('answer')