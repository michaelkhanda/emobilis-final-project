from django.contrib import admin

from main_app.models import HospitalAppointment, HospitalDepartment, HospitalDoctor


@admin.register(HospitalAppointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'patient_email', 'department', 'doctor', 'appointment_time', 'message']


@admin.register(HospitalDepartment)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(HospitalDoctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']
