from django.shortcuts import render,redirect

from common.models import Patient
from patient.models import Booking
from .models import * # we give * to import all model class from models.py
from django.core.mail import send_mail
from random import randint
from django.conf import settings # importing settings.py
import string
# Create your views here.

def admin_login(request):
    msg = ''   # declaring a variable

    if request.method == 'POST':

        user_name = request.POST['admin_id'] # username is variable, admin_id is textbox name in html page.
        password = request.POST['password']
        try: 
            data = AdminLogin.objects.get(admin_id = user_name ,
            admin_password = password)       # model name properties (models) = variablename(views)
            return redirect('hms_admin:admin_home') # redirect to home page

        except Exception as e:
            print(e)
            msg = 'Invalid User Name or Password'  # pass a message

            # we pass data form views to html in dictionary format in render()
    return render(request,'hms_admin/admin_login.html',{'error_msg':msg})   # keyvalue {'error_msg':msg}

def admin_home(request):
    return render(request,'hms_admin/admin_home.html')

def chg_pwd(request):
    return render(request,'hms_admin/admin_change_password.html')

def view_appointments(request):
    appointments = Booking.objects.all()
    return render(request,'hms_admin/view_appointments.html',{'appointments':appointments})

def add_doctor(request):
    error_msg = ''
    success_msg = ''

    departments = Department.objects.all()  # select * from department
    

    if request.method == 'POST':
        name = request.POST['doctor_name']
        email = request.POST['doctor_email']
        contact = request.POST['doctor_number']
        department = request.POST['doctor_dept']
        qualification = request.POST['qaulification']
        experience = request.POST['experience']
        fee = request.POST['fees']
        pic = request.FILES['doctor_photo']

        user_name = randint(1111,9999) # doctors username will be a unique 4 digit number
        password = 'doc-' + str(user_name) +'-' + contact[6:10]  # eg : password will be doc-3454-john 

        #  username and password will be sent to doctors email
        
        email_exist = Doctor.objects.filter(doctor_email = email).exists()
        if not email_exist:

            new_doctor = Doctor(doctor_name = name, doctor_email = email, doctor_contact = contact,department_id = department,
            qualification = qualification, experience = experience, fee = fee, pic = pic, username = user_name, password = password)
            new_doctor.save()
            success_msg = 'Doctor Added Succesfully'
        else:
            error_msg = 'Email Exists'    


         

        # send_mail(
        #     'username and password',
        #     'Hi, your username is '+ str(user_name) +' and password is ' + password,
        #     settings.EMAIL_HOST_USER,
        #     [email]
        # )
    return render(request,'hms_admin/add_doctor.html', {'departments':departments,'error_message' : error_msg, 'succes_message' : success_msg})

def consultion_details(request,dr_id):

    consultation_detail = Consultation.objects.filter(doctor = dr_id)
    doctor_name = Doctor.objects.filter(id = dr_id).values('doctor_name')[0]['doctor_name']
    error_msg = ''
    success_msg = ''


    if request.method == 'POST':

        consultaion_day = request.POST['consult_day']
        consultaion_time = request.POST['frm_time'] + ' - ' + request.POST['to_time']
        record_exist = Consultation.objects.filter(doctor = dr_id, day = consultaion_day, time = consultaion_time).exists()
        
        if not record_exist :
            new_record = Consultation(day = consultaion_day, time = consultaion_time, doctor_id = dr_id)
            new_record.save()
            success_msg = 'Record Added Succesfully'

        else:
            error_msg = 'Record Already Added'

    context = {
            'doctor_name': doctor_name,
            'consultation_detail': consultation_detail,
            'error_message' : error_msg,
            'success_message' :success_msg
                }
    return render(request,'hms_admin/consultation.html', context)


def doctors_list(request):
    doctors = Doctor.objects.filter(status = 'active')
    return render(request,'hms_admin/doctors_list.html',{'active_doctors' : doctors})

def view_report(request):
    return render(request,'hms_admin/view_report.html')

def view_patient(request):
    patient = Patient.objects.all()
    return render(request,'hms_admin/view_patient.html',{'patient':patient})

def add_department(request):
    error_msg = ''
    success_msg =''
    if request.method == 'POST':

        department = request.POST['dept'].lower()
        description = request.POST['desc']
        pic = request.FILES['pic']

        record_exist = Department.objects.filter(department = department).exists() # checking if the dept int table 
        # exist() give boolean result, that is true if data exist
        if not record_exist :

            new_dept = Department(department = department , description = description, pic = pic)
            new_dept.save()
            success_msg = 'Department Added Succesfully'
        else:
            error_msg = 'Department Exist'
            
    return render(request,'hms_admin/add_dept.html' , {'error_message' : error_msg, 'success_message' :success_msg})

def view_department(request):
    departments = Department.objects.all()
    return render(request,'hms_admin/departments.html', {'departments' :departments})


def add_staff(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['id']
        address = request.POST['address']
        phone = request.POST['number']
        password = request.POST['pass']
        pic = request.FILES['pic']
        # email_exist =  Staff.objects.filter(mail = mail, status = 'active').exists()
        staff = Staff(name = name, mail = mail,address = address, phone = phone, password = password, pic = pic)
        staff.save()
    return render(request,'hms_admin/add_staff.html')

def view_staff(request):
    staff = Staff.objects.filter(status = 'active')
    return render(request,'hms_admin/view_staff.html',{'staff':staff})

