from django.db import models
from django.urls import reverse

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=10)
    question = models.TextField()
    choices = [('Y', 'Yes'), ('N', 'No'), ('?', 'Not Sure')]
    answer = models.CharField(max_length=1, choices=choices)

    def get_absolute_url(self):
        return reverse('questions:question-list', kwargs={'id': self.id})