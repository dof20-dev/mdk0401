from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Grade
from .serializers import GradeSerializer


class GradeViewSet(viewsets.ModelViewSet):
    """CRUD для оценок."""
    queryset = Grade.objects.select_related("student", "subject", "teacher").all()
    serializer_class = GradeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["student", "subject", "value", "grade_type"]
    search_fields = ["student__full_name", "subject__name"]
    ordering_fields = ["date", "value", "created_at"]

    def perform_create(self, serializer):
        """Учитель = текущий пользователь."""
        serializer.save(teacher=self.request.user)
