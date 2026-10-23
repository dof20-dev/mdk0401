from django.db import models
from apps.accounts.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'teacher'})

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name

class Schedule(models.Model):
    STATUS_CHOICES = (
        ('planned', 'Запланирован'),
        ('completed', 'Проведен'),
        ('cancelled', 'Отменен'),
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    classroom = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='planned')

    class Meta:
        verbose_name = 'Урок (Расписание)'
        verbose_name_plural = 'Расписание уроков'

    def __str__(self):
        return f"{self.subject.name} - {self.date}"