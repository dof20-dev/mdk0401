from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Администратор"
        KEEPER = "keeper", "Кладовщик"
        MOL = "mol", "МОЛ"
        AUDITOR = "auditor", "Аудитор"

    full_name = models.CharField("ФИО", max_length=255, blank=True)
    role = models.CharField(
        "Роль", max_length=32,
        choices=Role.choices,
        default=Role.MOL,
    )

    def __str__(self):
        return self.full_name or self.username