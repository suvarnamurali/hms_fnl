from rest_framework import serializers
from patient.models import Presciption
 
 
class PrescriptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Presciption
        fields ='__all__'
