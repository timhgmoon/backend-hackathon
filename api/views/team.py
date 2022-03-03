from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import AttendeeSerializer
from django.shortcuts import get_object_or_404
from ..models import Attendee

class teamView(APIView):
  def get(self, request, team):
    attendees = Attendee.objects.filter(team=team)
    data = AttendeeSerializer(attendees, many=True).data
    return Response(data)