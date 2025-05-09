from django import forms
from .models import Booking,Contact, Users


class UserForm(forms.ModelForm):
    class Meta:
        model=Users
        fields = ['username','password']
        labels={
            'username': "USERNAME",
            'password': "PASSWORD"
        }
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }

    

class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets ={
            'booking_date': DateInput(),
        }


        labels ={
            'p_name' :"Patient Name",
            'p_phone' :"Patient Phone Number",
            'p_email' :"Patient E-mail",
            'doc_id' :"Please Selec Doctor",
            'booking_date' : "Pick a Date"
            
        }


class ContactForm(forms.ModelForm):
    class Meta :
        model= Contact
        fields = '__all__'


        labels = {
            'cleint_name' : "Enter Your Name",
            'cleint_email' : "Your E-mail",
            'cleint_message': "Your Message"
        }