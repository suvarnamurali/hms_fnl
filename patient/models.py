from django.db import models
from common.models import Patient
from hms_admin.models import Doctor


class Booking(models.Model) :
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True )
    patient_name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 10)
    mobile = models.BigIntegerField()
    age = models.IntegerField()
    reference_no = models.CharField(max_length = 30)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time = models.CharField(max_length = 10)
    booking_date = models.CharField(max_length = 20)
    status = models.CharField(max_length = 20, default = 'booked')

    class Meta : 
        db_table = 'booking_tb'


class Presciption(models.Model):
    booking = models.ForeignKey(Booking,on_delete = models.CASCADE)
    medicine_name = models.CharField(max_length = 20)
    days = models.IntegerField()
    prescription_notes = models.CharField(max_length = 100)
    

    class Meta : 
        db_table = 'prescription_tb'