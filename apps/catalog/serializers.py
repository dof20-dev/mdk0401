from rest_framework import serializers
from .models import Subject, Student


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "name", "teacher_name", "created_at"]
        read_only_fields = ["created_at"]


class StudentSerializer(serializers.ModelSerializer):
    class_name_display = serializers.CharField(source="get_class_name_display", read_only=True)
    status_display = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = Student
        fields = [
            "id", "full_name", "class_name", "class_name_display",
            "parent_phone", "birth_date", "status", "status_display", "created_at",
        ]
        read_only_fields = ["created_at"]
