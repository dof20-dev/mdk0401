from rest_framework import viewsets, filters
from .models import Teacher
from .serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """CRUD для учителей."""
    queryset = Teacher.objects.select_related("user").all()
    serializer_class = TeacherSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["user__username", "user__first_name", "user__last_name", "subject"]
    ordering_fields = ["created_at", "experience_years"]
