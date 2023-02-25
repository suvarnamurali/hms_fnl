from django.db import models

# Create your models here.

class Patient(models.Model):
    patient_name = models.CharField(max_length = 50)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.BigIntegerField()
    blood_grp = models.CharField(max_length=10)
    dob = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    status = models.CharField(max_length=20, default = 'active')
    pic = models.ImageField(upload_to = 'patient/', default = 'patient/default-user.png')

    class Meta :
        db_table = 'patient_tb'