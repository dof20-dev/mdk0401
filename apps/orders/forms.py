"""МОДУЛЬ 4: Формы для оценок."""
from django import forms
from .models import Grade


class GradeForm(forms.ModelForm):
    """Форма создания оценки."""

    class Meta:
        model = Grade
        fields = ["student", "subject", "value", "grade_type", "comment"]
        widgets = {
            "student": forms.Select(attrs={"class": "form-select"}),
            "subject": forms.Select(attrs={"class": "form-select"}),
            "value": forms.Select(attrs={"class": "form-select"}),
            "grade_type": forms.Select(attrs={"class": "form-select"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
