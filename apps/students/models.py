from django.db import models

class Student(models.Model):
    # Замени на строку:
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    full_name = models.CharField(max_length=200)
    class_number = models.CharField(max_length=10)
    parent_contact = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.class_number})"