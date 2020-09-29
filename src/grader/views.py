from django.shortcuts import render
from django.views.generic import CreateView

from .forms import GradeModelForm
from .models import Grade


class GradeCreateView(CreateView):
    template_name = "create_grade.html"
    form_class = GradeModelForm
