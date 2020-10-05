from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import GradeModelForm
from .models import Candidate, Grade


def grade_create_view(request):
    form = GradeModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = GradeModelForm()

    return render(request, "create_grade.html", {"form": form})


def candidates_grades_view(request):
    candidates_info = []
    for candidate in Candidate.objects.all():
        grades_val = [gr.value for gr in Grade.objects.filter(candidate=candidate)]
        candidates_info.append(
            {
                "pk": candidate.pk,
                "full_name": f"{candidate.first_name} {candidate.last_name}",
                "avg_grade": f"{sum(grades_val) / len(grades_val):.2f}",
                "grades": grades_val,
            }
        )
    return JsonResponse({"data": candidates_info})
