from django.db.models import Sum, Count, Avg
from django.utils import timezone
from datetime import timedelta
from apps.orders.models import Grade
from apps.catalog.models import Student, Subject


class ReportService:
    """Сервис отчётов по успеваемости."""

    @staticmethod
    def kpi(days: int = 30) -> dict:
        """Главные KPI журнала."""
        since = timezone.now() - timedelta(days=days)
        grades = Grade.objects.filter(created_at__gte=since)
        avg = grades.aggregate(avg=Avg("value"))["avg"] or 0
        count = grades.count()
        return {
            "avg_grade": round(float(avg), 2),
            "grades_count": count,
            "excellent": grades.filter(value=5).count(),
            "good": grades.filter(value=4).count(),
            "bad": grades.filter(value__lte=3).count(),
            "students_total": Student.objects.filter(status=Student.Status.ACTIVE).count(),
            "period_days": days,
        }

    @staticmethod
    def avg_by_day(days: int = 30) -> list:
        """Средний балл по дням."""
        since = timezone.now() - timedelta(days=days)
        rows = (
            Grade.objects.filter(created_at__gte=since)
            .extra(select={"day": "DATE(created_at)"})
            .values("day")
            .annotate(avg=Avg("value"), count=Count("id"))
            .order_by("day")
        )
        return [
            {"date": str(r["day"]), "avg": round(float(r["avg"]), 2), "count": r["count"]}
            for r in rows
        ]

    @staticmethod
    def top_subjects(limit: int = 5) -> list:
        """Топ предметов по среднему баллу."""
        rows = (
            Grade.objects.values("subject__name")
            .annotate(avg=Avg("value"), count=Count("id"))
            .order_by("-avg")[:limit]
        )
        return [
            {"subject": r["subject__name"], "avg": round(float(r["avg"]), 2), "count": r["count"]}
            for r in rows
        ]

    @staticmethod
    def teacher_load(days: int = 30) -> list:
        """Нагрузка учителей."""
        since = timezone.now() - timedelta(days=days)
        rows = (
            Grade.objects.filter(created_at__gte=since)
            .values("teacher__username")
            .annotate(count=Count("id"), avg=Avg("value"))
        )
        return [
            {
                "teacher": r["teacher__username"],
                "grades": r["count"],
                "avg": round(float(r["avg"]), 2),
            }
            for r in rows
        ]

    @staticmethod
    def class_stats() -> list:
        """Статистика по классам."""
        rows = (
            Student.objects.values("class_name")
            .annotate(count=Count("id"))
            .order_by("class_name")
        )
        return [{"class": r["class_name"], "count": r["count"]} for r in rows]
