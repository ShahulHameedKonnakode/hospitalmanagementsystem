from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    USER_TYPES=[
        ('admin','Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    user_type=models.CharField(max_length=50,choices=USER_TYPES)

class Department(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()
    dep_img = models.ImageField(upload_to='dep_images')

    def __str__(self):
        return self.dep_name


class Doctors(models.Model):
    user_id=models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr.' + self.user_id.get_full_name() +' | '+ self.doc_spec
    

class Booking(models.Model):
    doc_id = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=255)
    p_email = models.EmailField()    
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)


class Contact(models.Model):
    cleint_name = models.CharField(max_length=100)
    cleint_email = models.EmailField()
    cleint_message = models.TextField()

    def __str__(self):
        return self.cleint_name
    

class Prescription(models.Model):
    p_name=models.ForeignKey(Booking, on_delete=models.CASCADE)
    prescription=models.CharField(max_length=255)
    prescribed_by=models.ForeignKey(Doctors, on_delete=models.CASCADE)
    prescribed_on=models.DateTimeField(auto_now=True)