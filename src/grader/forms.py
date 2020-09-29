from django import forms

from .models import Grade


class GradeModelForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["value", "task", "candidate", "recruiter"]
