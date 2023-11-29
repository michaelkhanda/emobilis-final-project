from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def confirmation(request):
    return render(request, 'confirmation.html')


def appointment(request):
    return render(request, 'appointment.html')


def contact(request):
    return render(request, 'contact.html')


def department(request):
    return render(request, 'department.html')


def department_single(request):
    return render(request, 'department-single.html')


def doctor(request):
    return render(request, 'doctor.html')


def doctor_single(request):
    return render(request, 'doctor-single.html')


def service(request):
    return render(request, 'service.html')
