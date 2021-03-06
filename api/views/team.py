from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import AttendeeSerializer
from ..models import Attendee

class teamView(APIView):
  def get(self, request, team):
    attendees_by_team = Attendee.objects.filter(team=team)
    data = AttendeeSerializer(attendees_by_team, many=True).data
    return Response(data)