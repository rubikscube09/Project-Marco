from django.urls import path
from .views import (
    question_list_view,
    dynamic_lookup_view, 
    question_create_view    
    )

app_name = 'questions'
urlpatterns = [
    path('', question_list_view),
    path('genie/<int:id>/', dynamic_lookup_view, name='question-list'),
    path('create/', question_create_view),
]
