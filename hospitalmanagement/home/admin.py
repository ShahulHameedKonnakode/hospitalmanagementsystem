from django.contrib import admin
from .models import Users, Department,Doctors,Booking,Contact

# Register your models here.
admin.site.register(Users)
admin.site.register(Department)
admin.site.register(Doctors)
admin.site.register(Contact)

# class BookingAdmin(admin.ModelAdmin):
#     list_display=('id','p_name','p_phone','p_email','doc_name','booking_date','booked_on')
admin.site.register(Booking)



