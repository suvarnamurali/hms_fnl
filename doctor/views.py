import json
from django.shortcuts import render, redirect
from hms_admin.models import Doctor
from django.http import JsonResponse
from common.models import Patient
from patient.models import Booking
from datetime import datetime
from .serializers import *
from json import loads
from common.auth_guard import auth_doctor
# Create your views here.


@auth_doctor
def doctor_home(request):
    doctor = Doctor.objects.filter(
        id=request.session['doctor']).values('doctor_name')
    doc_name = doctor[0]['doctor_name']
    patients_count = Patient.objects.all().count()
   
   
    # today = datetime.strftime(datetime.today(),"%d-%m-%Y")
    today = "30-01-2023" 
     
    total_bookings = Booking.objects.filter(doctor = request.session['doctor'],booking_date = today, status = 'booked').count()
    print('jdwye',total_bookings)
    return render(request, 'doctor/doctor_home.html', {'doc_name': doc_name,'patients_count': patients_count, 'total_bookings' : total_bookings })


def profile(request):
    doctor = Doctor.objects.get(id=request.session['doctor'])
    return render(request, 'doctor/profile.html', {'doctor': doctor})


def edit_profile(request):
    doctor = Doctor.objects.get(id=request.session['doctor'])

    if request.method == 'POST':
        name = request.POST['dr_name']
        email = request.POST['dr_email']
        contact = request.POST['dr_contact']
        qualification = request.POST['dr_qual']
        experience = request.POST['dr_exp']
        fee = request.POST['dr_fee']

        doctor = Doctor.objects.get(id=request.session['doctor'])
        doctor.doctor_name = name
        doctor.doctor_email = email
        doctor.doctor_contact = contact
        doctor.qualification = qualification
        doctor.experience = experience
        doctor.fee = fee
        doctor.save()
        return redirect('doctor:dr_profile')

    return render(request, 'doctor/edit_profile.html', {'doctor': doctor})


def appointment(request):
     
    # today = datetime.strftime(datetime.today(), "%d/%m/%Y")
    today = "30-01-2023" 
    records = Booking.objects.filter(doctor = request.session['doctor'], status = 'booked',booking_date = today)

    return render(request, 'doctor/appointment.html',{'booking_records' : records})


def search_patients(request):
    patients_list = Patient.objects.all()
    return render(request, 'doctor/search_patients.html', {'patients_list': patients_list})




def change_password(request):

    error_msg = ''
    success_msg = ''

    if request.method == 'POST':

        old_password = request.POST['old_passwd']
        new_password = request.POST['new_passwd']
        confirm_password = request.POST['confirm_passwd']

        if new_password == confirm_password:
            if len(new_password) > 8:
                
                doctor = Doctor.objects.get(id=request.session['doctor'])
                
                if doctor.password == old_password:
                    doctor.password = new_password
                    doctor.save()
                    success_msg = 'Password Changed'
                
                else:
                    error_msg = 'Incorrect Password'

            else:
                error_msg = 'Password Should Be Min 8 Characters'

        else:
            error_msg = 'Password does\'nt match'

    return render(request, 'doctor/change_paswd.html', {'error_msg': error_msg, 'success_msg': success_msg})


def consulting(request):
    return render(request, 'doctor/consulting.html')


def get_patients(request):
    search_text = request.GET['search_text']
    
    search_result = Patient.objects.filter(patient_name__icontains = search_text)

    serialized_set = [{ 'id' : p.id, 'p_name' : p.patient_name.title() }  for p in search_result]
    return JsonResponse({'search_result' : serialized_set})


def patient_details(request,b_id):
    booking_record = Booking.objects.get(id = b_id) 
    
    return render(request,'doctor/patient_details.html', {'booking_record' : booking_record,})

def add_prescription(request,b_id):
    return render(request,'doctor/prescription.html', {'booking_id':b_id})

def submit_prescription(request):

    prescription = request.POST['prescription']
    

    prescription_obj=json.loads(prescription)

    print(prescription_obj[0]['booking'])
    bid=prescription_obj[0]['booking']
    booking=Booking.objects.get(id=bid)
 
    serialized_data = PrescriptionSerializer(data = prescription_obj,many = True)

    if serialized_data.is_valid():
        serialized_data.save()
        booking.status="consulted"
        booking.save()
        Booking.objects.filter(id = bid).update(status = 'completed')


    
    else :
        print('errore')
        print(serialized_data.errors)
    return JsonResponse(serialized_data.data,safe=False)

 