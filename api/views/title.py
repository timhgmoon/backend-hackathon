from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import AttendeeSerializer
from ..models import Attendee

class titleView(APIView):
  def get(self, request, title):
    attendees_by_title = Attendee.objects.filter(title=title)
    data = AttendeeSerializer(attendees_by_title, many=True).data
    return Response(data)