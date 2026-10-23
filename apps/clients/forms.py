"""МОДУЛЬ 3: Формы для учителей."""
from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):
    """Форма создания/редактирования учителя."""

    class Meta:
        model = Teacher
        fields = ["user", "subject", "phone", "experience_years"]
        widgets = {
            "user": forms.Select(attrs={"class": "form-select"}),
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "experience_years": forms.NumberInput(attrs={"class": "form-control"}),
        }
