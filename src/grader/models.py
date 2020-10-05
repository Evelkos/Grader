from django.db import models
from django.urls import reverse


class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Recruiter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Grade(models.Model):
    value = models.DecimalField(max_digits=3, decimal_places=0)
    task = models.ForeignKey("Task", on_delete=models.CASCADE)
    candidate = models.ForeignKey("Candidate", on_delete=models.CASCADE)
    recruiter = models.ForeignKey("Recruiter", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["task", "candidate"], name="assigned task")
        ]

    def __str__(self):
        return f"{self.recruiter}, {self.candidate}, {self.task}, {self.value}"

    def get_absolute_url(self):
        return reverse("grader:create_grade")


class Task(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"
