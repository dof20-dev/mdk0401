from rest_framework import serializers
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.get_full_name", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Teacher
        fields = [
            "id", "user", "user_name", "username", "subject",
            "phone", "experience_years", "created_at",
        ]
        read_only_fields = ["created_at"]
