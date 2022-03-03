from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import AttendeeSerializer
from django.shortcuts import get_object_or_404
from ..models import Attendee

class AttendeesView(APIView):
  def get(self, request):
    attendees = Attendee.objects.all()
    data = AttendeeSerializer(attendees, many=True).data
    return Response(data)