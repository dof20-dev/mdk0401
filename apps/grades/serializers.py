from rest_framework import serializers
from .models import Grade

class GradeSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.full_name')
    subject_name = serializers.ReadOnlyField(source='subject.name')
    class Meta:
        model = Grade
        fields = ['id', 'student', 'student_name', 'subject', 'subject_name', 'schedule', 'value', 'date', 'comment']
