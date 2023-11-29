from django import forms

from main_app.models import HospitalAppointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = HospitalAppointment
        fields = ['patient_name', 'patient_email', 'department', 'doctor', 'appointment_time', 'message']
