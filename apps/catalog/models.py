from django.db import models


class Subject(models.Model):
    """Учебный предмет."""
    name = models.CharField("Название", max_length=50, unique=True)
    teacher_name = models.CharField("Учитель", max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Student(models.Model):
    """Ученик."""

    class ClassName(models.TextChoices):
        A_5 = "5А", "5А"
        B_5 = "5Б", "5Б"
        A_9 = "9А", "9А"
        B_9 = "9Б", "9Б"
        A_11 = "11А", "11А"
        B_11 = "11Б", "11Б"

    class Status(models.TextChoices):
        ACTIVE = "active", "Учится"
        EXPELLED = "expelled", "Отчислен"
        GRADUATED = "graduated", "Выпустился"

    full_name = models.CharField("ФИО", max_length=100)
    class_name = models.CharField(
        "Класс", max_length=10,
        choices=ClassName.choices, default=ClassName.A_5,
    )
    parent_phone = models.CharField("Телефон родителя", max_length=20, blank=True)
    birth_date = models.DateField("Дата рождения", null=True, blank=True)
    status = models.CharField(
        "Статус", max_length=20,
        choices=Status.choices, default=Status.ACTIVE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"
        ordering = ["full_name"]

    def __str__(self):
        return f"{self.full_name} ({self.class_name})"

    @property
    def is_active(self):
        return self.status == self.Status.ACTIVE
