from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path("kpi/", views.KPIApiView.as_view(), name="kpi"),
    path("avg-by-day/", views.AvgByDayApiView.as_view(), name="avg_by_day"),
    path("top-subjects/", views.TopSubjectsApiView.as_view(), name="top_subjects"),
    path("teacher-load/", views.TeacherLoadApiView.as_view(), name="teacher_load"),
    path("class-stats/", views.ClassStatsApiView.as_view(), name="class_stats"),
]
