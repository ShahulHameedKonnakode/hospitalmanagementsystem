from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Department,Doctors, Users, Booking, Prescription
from .forms import BookingForm
from .forms import ContactForm,UserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.db.models import Prefetch




# Create your views here.


def logins(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
                login(request, user)
                request.session['admin_id']=user.id
                return redirect(admin_home)
        elif user is not None and user.user_type=='doctor':
                login(request, user)
                request.session['doctor_id']=user.id
                print("............",user.id)
                return redirect(doctor_home)
        elif user is not None and user.user_type=='patient' and user.is_active==1:
            login(request, user)
            request.session['patient_id']=user.id
            return redirect(reverse(admin_home))
    
    return render(request, 'login.html')


def logouts(request):
    logout(request)
    return redirect(index)

def admin_home(request):
    
    datas=Users.objects.all()
    return render(request,"admin_home.html",{'datas':datas})

def doctor_home(request):
    user_id=request.session.get("doctor_id")
    datas=Doctors.objects.get(user_id_id=user_id)
    return render(request,"doctor_home.html",{'datas':datas})

def departement_doctors(request):

    dept={
        'dep':Department.objects.all()
    }
    return render(request,'department_doctors.html',dept)

def doctors_doctors(request):
     doct={
        'doc':Doctors.objects.all()
    }  
     return render(request,'doctors_doctors.html',doct)

def appointment(request):

    appointments=Booking.objects.all()

    return render(request,'appointment.html',{'appointments': appointments})
from django.shortcuts import redirect
from django.db import transaction

@transaction.atomic
def prescription(request):
    if request.method == 'POST':
        try:
            booking_id = request.POST['patient_id']
            prescription_text = request.POST['prescription']
            doctor_id = request.POST['doc_id']
            
            # Verify the booking exists
            booking = Booking.objects.get(id=booking_id)
            # Verify the doctor exists
            doctor = Doctors.objects.get(id=doctor_id)
            
            prescriptions = Prescription.objects.create(
                p_name_id=booking_id,
                prescription=prescription_text, 
                prescribed_by_id=doctor.id
            )
            return redirect('doctor_home')  # Redirect to doctor home or success page
        except (Booking.DoesNotExist, Doctors.DoesNotExist) as e:
            return render(request, 'error.html', {'error': 'Invalid ID provided'})
        except Exception as e:
            return render(request, 'error.html', {'error': str(e)})
    
    return render(request, 'index.html')

def add_doctors(request):
     if request.method=='POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        email= request.POST['email']
        department= request.POST['dep_id']
        specialization=request.POST['specialization']
        photo= request.FILES['photo']
        print(first_name,last_name,username,password,email,department,photo)
        doctor_user= Users.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email,user_type='doctor')
        doctor_user.save()
        doctor_datas=Doctors.objects.create(user_id=doctor_user,doc_spec=specialization,dep_name_id=department,doc_image=photo)
        doctor_datas.save()
          


     departments=Department.objects.all()
     return render(request,"add_doctors_admin.html",{'departments':departments})

def index(request):
     doct={
        'doc':Doctors.objects.all()
    }  
    
     return render(request, 'index.html',doct)

def about(request):
    return render(request, 'about.html')

def booking_admin(request):
    if request.method =="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            last_entry=form.save()            
            
            return render(request,'confirmation.html',{'last_entry':last_entry})

    form = BookingForm()
    dic_form={
        'form':form
    }
    return render(request, 'booking_admin.html',dic_form)


def booking_patient(request):
    if request.method =="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            last_entry=form.save()            
            
            return render(request,'confirmation.html',{'last_entry':last_entry})

    form = BookingForm()
    dic_form={
        'form':form
    }
    return render(request, 'booking_patient.html',dic_form)

def doctors(request):  

     doct={
        'doc':Doctors.objects.all()
    }  
     return render(request, 'doctors.html',doct)

def contact(request):

    if request.method== "POST":
        form=ContactForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')


    form=ContactForm()
    dict_contact = {
        'form':form
    }

    return render(request, 'contact.html',dict_contact)

def department(request):

    dept={
        'dep':Department.objects.all()
    }
    return render(request,'department.html',dept)


def confirmation(request):
      booking_details =Booking.objects.last()
      
            
      return render(request,'confirmation.html',{'last_entry':booking_details})
    

def doctors_section(request): 
   
    return render(request,'doctors_section.html')
