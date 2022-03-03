from django.urls import path
from .views import attendees
from .views import team
from .views import company
from .views import title

urlpatterns = [
  path('api/', attendees.AttendeesView.as_view(), name='index'),
  path('api/<int:pk>/', attendees.AttendeeView.as_view()),
  path('api/team/<int:team>/', team.teamView.as_view()),
  path('api/Company/<str:company>/', company.companyView.as_view()),
  path('api/title/<str:title>/', title.titleView.as_view()),
]