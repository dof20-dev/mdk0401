from django.db import models
from django.conf import settings


class Teacher(models.Model):
    """Профиль учителя (расширение User)."""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="teacher_profile",
        verbose_name="Пользователь",
    )
    subject = models.CharField("Основной предмет", max_length=100, blank=True)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    experience_years = models.PositiveIntegerField("Стаж, лет", default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
        ordering = ["user__last_name"]

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} ({self.subject})"
