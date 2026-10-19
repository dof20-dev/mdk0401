from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    # Вместо from apps.accounts.models import User пишем строку:
    teacher = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'teacher'})

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

    def __str__(self):
        return f"{self.subject.name} - {self.date}"