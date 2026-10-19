from django.db import models

class Grade(models.Model):
    # Используем строковые ссылки на модели ('students.Student' и 'schedule.Subject'), 
    # чтобы Django не падал при загрузке
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    subject = models.ForeignKey('schedule.Subject', on_delete=models.CASCADE)
    schedule = models.ForeignKey('schedule.Schedule', on_delete=models.CASCADE, null=True, blank=True)
    
    value = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    date = models.DateField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.schedule:
            self.schedule.status = 'completed'
            self.schedule.save()

    def __str__(self):
        return f"{self.student.full_name} - {self.subject.name}: {self.value}"