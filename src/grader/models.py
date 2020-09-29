from django.db import models


class Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Recruiter(models.Model):
    recruiter_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Grade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=3, decimal_places=0)
    task = models.ForeignKey("Task", on_delete=models.CASCADE)
    candidate = models.ForeignKey("Candidate", on_delete=models.CASCADE)
    recruiter = models.ForeignKey("Recruiter", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recruiter}, {self.candidate}, {self.task}, {self.value}"


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"