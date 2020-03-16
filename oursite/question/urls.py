from django.urls import path
from .views import (
    question_list_view,
    dynamic_lookup_view, 
    question_location,
    update_origin_info,
    get_cities,
    start_date_view,
    num_travelers_view,
    duration_view
    )

app_name = 'questions'
urlpatterns = [
    path('', question_list_view),
    path('<int:id>/', dynamic_lookup_view, name='question-list'),
    path('getting-started/', question_location),
    path('origin/', update_origin_info),
    path('date/', start_date_view),
    path('genie/<int:id>/', get_cities),
    path('num_travelers/', num_travelers_view),
    path('duration/', duration_view)
]
