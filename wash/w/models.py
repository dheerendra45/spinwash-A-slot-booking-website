from django.db import models

class Complaint(models.Model):
    full_name = models.CharField(max_length=255)
    hostel_name = models.CharField(max_length=255)
    email = models.EmailField()
    machine_model = models.CharField(max_length=255, blank=True, null=True)
    problem_description = models.TextField()


    def __str__(self):
        return self.full_name

class HostelSlot(models.Model):
    booking_date = models.DateField()
    hostel_name = models.CharField(max_length=50)
    machine_number = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.hostel_name} - Machine {self.machine_number} - {self.booking_date} ({self.start_time} to {self.end_time})"


class CustomerBooking(models.Model):
    booking_date = models.DateField()
    hostel_name = models.CharField(max_length=50)
    machine_number = models.IntegerField()
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.hostel_name} - Machine {self.machine_number} - {self.booking_date} ({self.start_time} to {self.end_time})"