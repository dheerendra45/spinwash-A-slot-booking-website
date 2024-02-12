from django.db import models

class Complaint(models.Model):
    full_name = models.CharField(max_length=255)
    hostel_name = models.CharField(max_length=255)
    email = models.EmailField()
    machine_model = models.CharField(max_length=255, blank=True, null=True)
    problem_description = models.TextField()

    def __str__(self):
        return self.full_name