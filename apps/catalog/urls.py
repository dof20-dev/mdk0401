from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, StudentViewSet

router = DefaultRouter()
router.register("subjects", SubjectViewSet, basename="subjects")
router.register("students", StudentViewSet, basename="students")

urlpatterns = [
    path("", include(router.urls)),
]
