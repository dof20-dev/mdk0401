from rest_framework.views import APIView
from rest_framework.response import Response
from .services import ReportService


class KPIApiView(APIView):
    """GET /api/reports/kpi/?days=30"""
    def get(self, request):
        days = int(request.GET.get("days", 30))
        return Response(ReportService.kpi(days))


class AvgByDayApiView(APIView):
    """GET /api/reports/avg-by-day/?days=30"""
    def get(self, request):
        days = int(request.GET.get("days", 30))
        return Response(ReportService.avg_by_day(days))


class TopSubjectsApiView(APIView):
    """GET /api/reports/top-subjects/?limit=5"""
    def get(self, request):
        limit = int(request.GET.get("limit", 5))
        return Response(ReportService.top_subjects(limit))


class TeacherLoadApiView(APIView):
    """GET /api/reports/teacher-load/?days=30"""
    def get(self, request):
        days = int(request.GET.get("days", 30))
        return Response(ReportService.teacher_load(days))


class ClassStatsApiView(APIView):
    """GET /api/reports/class-stats/"""
    def get(self, request):
        return Response(ReportService.class_stats())
