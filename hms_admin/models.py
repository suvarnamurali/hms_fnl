from django.db import models

# Create your models here.

class AdminLogin(models.Model):
    admin_id = models.CharField(max_length = 50)
    admin_password = models.CharField(max_length = 20)
 
    class Meta :
        db_table = 'admin_tb'


class Department(models.Model):
    department = models.CharField(max_length = 50)
    description = models.CharField(max_length=2000)
    pic = models.ImageField(upload_to = 'department/')

    class Meta :
        db_table = 'dept_tb'



class Doctor(models.Model):
    doctor_name = models.CharField(max_length = 50)
    doctor_email = models.CharField(max_length = 50)
    doctor_contact = models.CharField(max_length = 50)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    qualification = models.CharField(max_length = 50)
    experience = models.CharField(max_length = 50)
    fee = models.CharField(max_length = 50)
    pic = models.ImageField(upload_to = 'doctor/')
    username = models.IntegerField()
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default = 'active')
    
    class Meta :
        db_table = 'doctr_tb'


class Staff(models.Model):
    name = models.CharField(max_length = 50)
    mail = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    pic = models.ImageField(upload_to = 'staff/')
    status = models.CharField(max_length=20, default = 'active')
    
    class Meta :
        db_table = 'staff_tb'

class Consultation(models.Model) : 

    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    day = models.CharField(max_length = 20)
    time = models.CharField(max_length = 20)
    status = models.CharField(max_length = 20, default = 'available')
    
    class Meta :
        db_table = 'consult_tb'