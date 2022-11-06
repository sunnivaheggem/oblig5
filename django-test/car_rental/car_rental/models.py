from django.db import models

class Car(models.Model):
    make = models.CharField(max_length = 50) 
    carmodel = models.CharField(max_length = 50)
    year = models.CharField(max_length = 10) 
    location = models.CharField(max_length = 50)
    status = models.CharField(max_length = 50) 
    condition = models.CharField(max_length = 50) 

    def __str1__(self):
        return self.make + ' '+ + self.carmodel + ' '+ + self.year + ' '+ + self.location + ' '+ + self.status + ' '+ + self.condition

class Customer(models.Model):
    name = models.CharField(max_length = 50) 
    age = models.CharField(max_length = 3)
    address = models.CharField(max_length = 50)
    customer_status = models.OneToOneField(Car, on_delete=models.SET_NULL, null=True, blank=True)


    def __str2__(self):
        return self.name + ' '+ + self.age + ' '+ + self.address + ' '+ + self.customer_status

class Employee(models.Model):
    name = models.CharField(max_length = 50) 
    branch = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50) 

    def __str3__(self):
        return self.name + ' '+ + self.branch + ' '+ + self.address