from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
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
        '''
        Get the absolute url to a question on the list questions page.

        Input: None

        Output: An absolute url
        '''

        return reverse('questions:question-list', kwargs={'id': self.id})
    

    def clean_answer(self):
        '''
        Get the cleaned answer
        '''

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
        '''
        Get the cleaned answer
        '''

        answer = self.clean_data.get('answer')
    

    def clean(self):
        '''
        Validate the starting and end dates, raise an error if the starting
        date is later than the end date.
        '''

        if self.start_date > self.end_date:
            raise ValidationError('Please choose another date')