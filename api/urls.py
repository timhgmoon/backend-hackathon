from django.urls import path
from .views import attendees

urlpatterns = [
  path('api/', attendees.AttendeesView.as_view(), name='index'),
]