from django.contrib.auth import logout

from django.shortcuts import render,redirect

from .models import Complaint,CustomerBooking,HostelSlot
from django.http import HttpResponseRedirect


def home(request):
    return render(request, "home.html")


def index(request):
    return render(request,"index.html")
def book(request):
    return render(request,"book1.html")
def support(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        hostel_name = request.POST['hostel_name']
        email = request.POST['email']
        machine_model = request.POST.get('machine_model', '')
        problem_description = request.POST['problem_description']


        complaint = Complaint(
            full_name=full_name,
            hostel_name=hostel_name,
            email=email,
            machine_model=machine_model,
            problem_description=problem_description
        )
        complaint.save()




        return HttpResponseRedirect('/success')
    return render(request,"support.html")
def logout_view(request):
    logout(request)
    return redirect('/book')

def success(request):
    return render(request,"success.html")
