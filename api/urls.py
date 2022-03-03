from django.urls import path
from .views import attendees
from .views import team

urlpatterns = [
  path('api/', attendees.AttendeesView.as_view(), name='index'),
  path('api/<int:pk>/', attendees.AttendeeView.as_view()),
  path('api/team/<int:team>/', team.teamView.as_view()),
]