from django.db import models
from hms_admin.models import Doctor
# Create your models here.
 

class Consultion(models.Model) : 

    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    day = models.CharField(max_length = 20)
    time = models.CharField(max_length = 20)

 