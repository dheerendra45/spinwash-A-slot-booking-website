from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'hostel_name', 'email', 'machine_model', 'problem_description']
    search_fields = ['full_name', 'hostel_name', 'email', 'machine_model', 'problem_description']