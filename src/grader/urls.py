from django.contrib import admin
from django.urls import path

from .views import GradeCreateView

urlpatterns = [path("create/grade/", GradeCreateView.as_view())]
