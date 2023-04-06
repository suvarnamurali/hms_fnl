from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('departments', views.dept, name='depts'),
    path('services', views.service, name='services'),
    path('department/<int:id>', views.department_details, name='department_details'),
    path('doctor/<int:id>', views.doctor_details, name='doctor_details'),
    path('doctor', views.doctor, name='dr'),
    path('user-type', views.user_type, name='user_type'),
    path('login', views.login, name='login'),
    path('register', views.patient_registration, name='pat_register'),
    path('make-appointment',views.make_appointment,name = 'make_appointment'),
    path('forgot_pass',views.forgot_pass,name = 'forgot_pass'),
    path('reset_pass',views.reset_pass,name = 'reset_pass')
]