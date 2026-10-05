from django.contrib import admin
from .models import Grade


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "value", "grade_type", "teacher", "date")
    list_filter = ("value", "grade_type", "subject", "date")
    search_fields = ("student__full_name", "subject__name")
    readonly_fields = ("created_at",)
