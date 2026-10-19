from rest_framework import serializers
from .models import Subject, Schedule

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    subject_name = serializers.ReadOnlyField(source='subject.name')
    
    class Meta:
        model = Schedule
        fields = ['id', 'subject', 'subject_name', 'date', 'time', 'classroom', 'status']