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

class AttendeeView(APIView):
  def get(self, request, pk):
    attendee = get_object_or_404(Attendee, pk=pk)
    data = AttendeeSerializer(attendee).data
    return Response(data)

  def put(self, request, pk):
    attendee = get_object_or_404(Attendee, pk=pk)
    data = AttendeeSerializer(attendee, data=request.data, partial=True)
    if data.is_valid():
      data.save()
      return Response(data.data, status=status.HTTP_202_ACCEPTED)
    return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
    attendee = get_object_or_404(Attendee, pk=pk)
    data = AttendeeSerializer(attendee).data
    attendee.delete()
    return Response(data)