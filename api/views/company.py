from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import AttendeeSerializer
from ..models import Attendee

class companyView(APIView):
  def get(self, request, company):
    attendees_by_company = Attendee.objects.filter(Company=company)
    data = AttendeeSerializer(attendees_by_company, many=True).data
    return Response(data)