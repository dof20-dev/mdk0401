from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("user", "subject", "phone", "experience_years", "created_at")
    search_fields = ("user__username", "user__last_name", "subject")
    list_filter = ("subject", "created_at")
