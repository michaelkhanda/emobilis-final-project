from django.db import models


class HospitalDepartment(models.Model):
    name = models.CharField(max_length=255)


class HospitalDoctor(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(HospitalDepartment, on_delete=models.CASCADE)


class HospitalAppointment(models.Model):
    patient_name = models.CharField(max_length=255)
    patient_email = models.EmailField()
    department = models.ForeignKey(HospitalDepartment, on_delete=models.CASCADE)
    doctor = models.ForeignKey(HospitalDoctor, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    message = models.TextField()
