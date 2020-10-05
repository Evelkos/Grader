from django.contrib import admin
from django.urls import path

from .views import candidates_grades_view, grade_create_view

app_name = "grader"
urlpatterns = [
    path("add-mark/", grade_create_view, name="create_grade"),
    path("get-candidates/", candidates_grades_view, name="get_candidates"),
]
