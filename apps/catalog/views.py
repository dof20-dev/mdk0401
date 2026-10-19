"""ViewSet автоматически создаёт все CRUD-эндпоинты."""

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Subject, Student
from .serializers import SubjectSerializer, StudentSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    """CRUD для предметов."""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "teacher_name"]


class StudentViewSet(viewsets.ModelViewSet):
    """CRUD для учеников с фильтрами."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["class_name", "status"]
    search_fields = ["full_name", "parent_phone"]
    ordering_fields = ["full_name", "class_name", "created_at"]
