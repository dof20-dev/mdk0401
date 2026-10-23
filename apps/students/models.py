from django.db import models
from apps.accounts.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    full_name = models.CharField(max_length=200)
    class_number = models.CharField(max_length=10)
    parent_contact = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return f"{self.full_name} ({self.class_number})"