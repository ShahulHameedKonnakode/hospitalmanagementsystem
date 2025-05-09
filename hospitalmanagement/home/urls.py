from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('doctor_home', views.doctor_home, name='doctor_home'),
    path('add_doctors', views.add_doctors, name='add_doctors'),
    

    
    path('logins', views.logins, name='logins'),
    path('about', views.about, name='about'),
    path('booking_admin', views.booking_admin, name='booking_admin'),
    path('booking_patient', views.booking_patient, name='booking_patient'),
    path('doctors', views.doctors, name='doctors'),
    path('doctors_doctors', views.doctors_doctors, name='doctors_doctors'),
    path('contact', views.contact, name='contact'),
    path('department', views.department, name='department'),
    path('departement_doctors', views.departement_doctors, name='departement_doctors'),
    path('appointment', views.appointment, name='appointment'),
    path('prescription', views.prescription, name='prescription'),

    
    
    
    path('logouts', views.logouts, name='logouts'),
    # path('doctors_section', views.doctors_section,name='doctors_section')
    # path('confirmation', views.confirmation, name='confirmation')


]
