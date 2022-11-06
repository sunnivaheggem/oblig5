from django.contrib import admin 
from .models import Car
from .models import Customer
from .models import Employee

# Register your models here. 
admin.site.register(Car)

admin.site.register(Customer)

admin.site.register(Employee)
