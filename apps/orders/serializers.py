from rest_framework import serializers
from .models import Grade


class GradeSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.full_name", read_only=True)
    subject_name = serializers.CharField(source="subject.name", read_only=True)
    teacher_name = serializers.CharField(source="teacher.get_full_name", read_only=True)
    value_display = serializers.CharField(source="get_value_display", read_only=True)
    grade_type_display = serializers.CharField(source="get_grade_type_display", read_only=True)

    class Meta:
        model = Grade
        fields = [
            "id", "student", "student_name", "subject", "subject_name",
            "teacher", "teacher_name", "value", "value_display",
            "grade_type", "grade_type_display", "date", "comment", "created_at",
        ]
        read_only_fields = ["teacher", "date", "created_at"]
