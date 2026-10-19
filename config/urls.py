from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.reports.views import KPIAvgView  # <-- Добавили импорт

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Наши API
    path('api/', include('apps.schedule.urls')),
    path('api/', include('apps.students.urls')),
    path('api/', include('apps.grades.urls')),
    
    # Отчеты (KPI)
    path('api/reports/kpi/', KPIAvgView.as_view()),  # <-- Добавили путь
    
    # Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # JWT
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]