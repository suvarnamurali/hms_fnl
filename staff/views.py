from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.db.models import Q
from django.template.loader import render_to_string
from common.models import Patient
from patient.models import Booking

# Create your views here.
def staff_home(request):
    return render(request,'staff/staff_home.html')



def appointments(request):
    booking = Booking.objects.all()
    return render(request,'staff/appointments.html',{'booking':booking})

def registration(request):

    error_msg = ''
    success_msg = ''
    if request.method == 'POST':

        name = request.POST['p_name']
        address = request.POST['p_address']
        age = request.POST['p_age']
        blood_group = request.POST['p_blood']
        contact = request.POST['p_contact']
        dob = request.POST['p_dob']
        gender = request.POST['gender']
        email = request.POST['p_mail']

        record_exist = Patient.objects.filter(email = email).exists()

        if not record_exist :
            if 'pic' in request.FILES : # here pic is the name attribute of fileuploader
                pic = request.FILES['pic']
        
                patient_record = Patient( patient_name = name ,email = email, address = address , age = age , blood_grp = blood_group , 
                phone = contact , dob = dob , gender = gender , pic = pic )
                
            else :

                patient_record = Patient( patient_name = name ,email = email, address = address , age = age , blood_grp = blood_group , 
                phone = contact , dob = dob , gender = gender )

            
            patient_record.save()
            success_msg = 'Record Added Succesfully'

        else:
            error_msg = 'Email Exists'

    return render(request,'staff/registration.html',{'success_msg':success_msg,'error_msg':error_msg})

def patient_search(request):
    patient = Patient.objects.all()
    return render(request,'staff/patient_search.html',{'patient':patient})
   
def booking_list(request):
    bookings = Booking.objects.filter(Q(status = 'booked') | Q(status = 'completed'))
     
    if request.method == 'POST':
        reference_no = request.POST['reference_no']

        search_result = Booking.objects.filter(reference_no__icontains = reference_no)
        print(search_result,'lll')
        html = render_to_string(
            template_name="staff/booking_partial.html", 
            context={"bookings": search_result}
        )

        data_dict = {"result": html}

        return JsonResponse(data=data_dict, safe=False)

    
    return render(request,'staff/bookings.html',{'bookings':bookings})

def profile(request):
    
    return render(request,'staff/staff_profile.html')

def logout(request):
    del request.session['staff']
    request.session.flush()
    return redirect('common:com-home')


    
