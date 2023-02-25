from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('home', views.doctor_home, name='dr_home'), 
    path('profile', views.profile, name='dr_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('appointment/', views.appointment, name='appointment'),
    path('search/patients',views.search_patients,name='search_patients'),
    path('change_password',views.change_password,name='change_pswd'),
    path('consulting',views.consulting,name='consulting'),
    path('patient/list',views.get_patients,name='get_patients'),
    path('prescription/<int:b_id>',views.add_prescription,name='add_prescription'),
    path('booking/<int:b_id>',views.patient_details,name='patient_details'),
    path('booking-submit',views.submit_prescription,name='submit_prescription'),

    

]