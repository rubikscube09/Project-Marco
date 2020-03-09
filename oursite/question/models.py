from django.db import models
from django.urls import reverse

# Create your models here.
class Question(models.Model):
    question = models.TextField()
    choices = [('Y', 'YES'), ('N', 'NO'), ('?', 'NOT SURE')]
    answer = models.CharField(max_length=1, choices=choices)
    test = models.CharField(max_length=2)

    def get_absolute_url(self):
        return reverse('questions:question-list', kwargs={'id': self.id})