from django.contrib import admin
from .models import Candidate, Recruiter, Grade, Task


admin.site.register(Candidate)
admin.site.register(Recruiter)
admin.site.register(Grade)
admin.site.register(Task)
