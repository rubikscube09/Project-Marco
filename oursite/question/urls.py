from django.urls import path
from .views import (
    question_list_view,
    dynamic_lookup_view, 
    question_location,
    update_origin_info
    )

app_name = 'questions'
urlpatterns = [
    path('', question_list_view),
    path('genie/<int:id>/', dynamic_lookup_view, name='question-list'),
    path('getting-started/', question_location),
    path('origin/', update_origin_info),
    path('test/', )
]