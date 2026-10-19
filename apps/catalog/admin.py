from django.contrib import admin
from .models import Subject, Student


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher_name", "created_at")
    search_fields = ("name",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "class_name", "parent_phone", "status")
    list_filter = ("class_name", "status")
    search_fields = ("full_name", "parent_phone")
    list_editable = ("status",)
