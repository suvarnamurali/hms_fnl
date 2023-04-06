import string
from django.shortcuts import render,redirect,reverse
from hms_admin.models import Staff,Doctor
from .models import Patient
from hms_admin.models import Department
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def index(request):
    return render(request,'common/index.html')

def user_type(request):
    return render(request,'common/user_type.html')    
 
def about(request):
    return render(request,'common/about.html')

def contact(request):
    return render(request,'common/contact.html')

def dept(request):
    departments = Department.objects.all()
     
    return render(request,'common/department.html',{'departments':departments,})

def service(request):
    return render(request,'common/service.html')


def patient_registration(request):

    error_msg = ''
    success_msg = ''
    if request.method == 'POST':

        name = request.POST['pat_name']
        address = request.POST['pat_address']
        age = request.POST['pat_age']
        blood_group = request.POST['blood_grp']
        contact = request.POST['pat_phno']
        dob = request.POST['pat_dob']
        gender = request.POST['gender']
        email = request.POST['pat_email']

        record_exist = Patient.objects.filter(email = email).exists() # checking if the email entereb by the user exists

        if not record_exist :
            # if user uploaded the picture, then the user picture is upload, other wise a dummy image is saved which is saved in static folder 
            if 'pic' in request.FILES : # here pic is the name attribute of fileuploader
                pic = request.FILES['pic']
        
                patient_record = Patient( patient_name = name ,email = email, address = address , age = age , blood_grp = blood_group , 
                phone = contact , dob = dob , gender = gender , pic = pic)
                
            else :

                patient_record = Patient( patient_name = name ,email = email, address = address , age = age , blood_grp = blood_group , 
                phone = contact , dob = dob , gender = gender )

            
            patient_record.save()
            success_msg = 'Record Added Succesfully'

        else:
            error_msg = 'Email Exists'
    return render(request,'common/patient_register.html', {'success_msg' : success_msg, 'error_msg' : error_msg})

def login(request):

    user_type = request.GET['user'] # getting query string value from url
    msg = ''
    
     

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if user_type ==  'staff':
             
            try :
                staff = Staff.objects.get(mail = username, password = password)

                if staff.status == 'active':

                    request.session['staff'] = staff.id # setting session for staff
                    request.session['pic'] = staff.pic.url
                    return redirect('staff:staff_home')
                else:
                    msg = 'Account Inactive'
            except :
                msg = 'Invalid Username Or Password'

        if user_type == 'doc':
             
            try :
                doctor = Doctor.objects.get(username = username, password = password)
                request.session['doctor'] = doctor.id
                return redirect('doctor:dr_home')
            except :
                msg = 'Invalid Username Or Password'
        
        if user_type == 'patient':
             
            try :
                patient = Patient.objects.get(email = username, phone = password)
                request.session['patient'] = patient.id
                # if not patient.pic.url == 'static/default-user.png':
                #     print('truee')
                request.session['pic'] = patient.pic.url
                # else:
                #     request.session['pic'] = 'static/default-user.png'

                return redirect('patient:home')
      
            except:
                msg = 'Invalid Username Or Password'

        
    return render(request,'common/login.html', {'error_msg' : msg,'user_type':user_type})

def department_details(request,id):
    department = Department.objects.get(id = id)
    doctors = Doctor.objects.filter(department = id)
    return render(request,'common/department_details.html',{ 'department': department,'doctors' : doctors})

def doctor_details(request,id):
    doctor = Doctor.objects.get(id = id)
    return render(request,'common/doctor_details.html',{'doctor': doctor,})

def doctor(request):
    return render(request,'common/hms_doctor.html')


def make_appointment(request):
 
    if 'patient' in request.session:
        return redirect('patient:appointment_1') 

  
    request.session['log'] = True
    return redirect(reverse('common:login') + '?user=patient') 



def forgot_pass(request):
    
    user_type = request.GET.get('user')
    msg=""
    if request.method=='POST':
        email=request.POST['email']
        
        if user_type=='doc':
             user = Doctor.objects.filter(doctor_email= email)               
            
        if user_type=='patient':
            user = Patient.objects.filter(email=email)

        if user_type=='staff' :
            user = Staff.objects.filter(mail=email)

        print('999',user_type)

        if  user.exists():
            print(user[0])
            print(user[0].id)
            uid=user[0].id    
            message="password reset link  http://127.0.0.1:8000/reset_pass?user=" + user_type + "&id=" + str(uid)
            print(message)
            send_mail(
                'password reset',
                message,
                settings.EMAIL_HOST_USER,
                [user[0].email],
                fail_silently=False)
            
            print('succsess')
        else:
            msg="user not exist"


    return render(request,'common/forgot_pass.html',{'error':msg})

    

def reset_pass(request):
    msg=""
    user_type = request.GET.get('user')
    id=int(request.GET.get('id'))
    if request.method=='POST':
        password=request.POST['password']

        if user_type=='doc':
            user = Doctor.objects.get(id=id)     
            
        if user_type=='patient':
            user = Patient.objects.get(id=id)
            
        if user_type=='staff' :
            user = Staff.objects.get(id=id)


        
        user.password = password
        user.save()
        msg="pasword reset successfull"

    return render(request,'common/reset_pass.html',{'msg':msg})
