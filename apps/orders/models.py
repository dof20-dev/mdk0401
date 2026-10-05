from django.db import models
from django.conf import settings
from apps.catalog.models import Subject, Student


class Grade(models.Model):
    """Оценка ученика по предмету."""

    class Value(models.IntegerChoices):
        TWO = 2, "2 (неудовлетворительно)"
        THREE = 3, "3 (удовлетворительно)"
        FOUR = 4, "4 (хорошо)"
        FIVE = 5, "5 (отлично)"

    class GradeType(models.TextChoices):
        CURRENT = "current", "Текущая"
        TEST = "test", "Контрольная"
        HOMEWORK = "homework", "Домашняя"
        FINAL = "final", "Итоговая"

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name="grades", verbose_name="Ученик",
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.PROTECT,
        related_name="grades", verbose_name="Предмет",
    )
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="grades", verbose_name="Учитель",
    )
    value = models.IntegerField("Оценка", choices=Value.choices)
    grade_type = models.CharField(
        "Тип", max_length=20,
        choices=GradeType.choices, default=GradeType.CURRENT,
    )
    date = models.DateField("Дата", auto_now_add=True)
    comment = models.TextField("Комментарий", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.student.full_name} — {self.subject.name}: {self.value}"
