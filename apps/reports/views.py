from rest_framework.views import APIView
from rest_framework.response import Response
from apps.grades.models import Grade
from django.db.models import Avg

class KPIAvgView(APIView):
    def get(self, request):
        avg_grade = Grade.objects.aggregate(Avg('value'))
        return Response({"average_grade": avg_grade['value__avg']})
