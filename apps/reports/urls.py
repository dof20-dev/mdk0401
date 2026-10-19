from django.contrib import admin
from django.urls import path, include
from apps.reports.views import KPIAvgView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.accounts.urls')),
    path('api/', include('apps.schedule.urls')),
    path('api/', include('apps.students.urls')),
    path('api/', include('apps.grades.urls')),
    path('api/reports/', KPIAvgView.as_view()),
]