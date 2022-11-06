from .models import Car
from .models import Customer
from .models import Employee
from rest_framework.response import Response 
from .serializers import CarSerializer
from .serializers import CustomerSerializer
from .serializers import EmployeeSerializer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_customer(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_employee(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def save_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def save_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def save_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_car(request, id):
    try: 
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CarSerializer(theCar, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) 
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_customer(request,id):
    try: 
        theCustomer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(theCustomer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) 
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_employee(request, id):
    try: 
        theEmployee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EmployeeSerializer(theEmployee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) 
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    theCar.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def delete_customer(request, id):
    try:
        theCustomer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    theCustomer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def delete_employee(request, id):
    try:
        theEmployee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    theEmployee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view (['POST'])
def order_car(car_id, customer_id):
    try: 
        Car_object = Car.objects.get(pk = car_id)
        Customer_object = Customer.objects.get(pk = customer_id) 
        if Car_object.status == 'available' and Customer_object.customer_status == None : #sjekker at bilen er booket, og at det er kunden som har booket den
            Car_object.status = 'booked'
            Customer_object.customer_status = Car_object
    except Car_object.DoesNotExist or Customer_object.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    Car_object.save()
    Customer_object.save()
    return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def cancel_order_car(car_id, customer_id):
    try: 
        Car_object = Car.objects.get(pk=car_id)
        Customer_object= Customer.objects.get(pk=customer_id) 
        if Car_object.status == 'booked' and Customer_object.customer_status == Car_object: #sjekker at bilen står som booket og at kunden er den som har booket den
            Car_object.status = "available"
            Customer_object.customer_status = None
    except Car_object.DoesNotExist or Customer_object.DoesNotExist:
       return Response(status = status.HTTP_404_NOT_FOUND)
    Car_object.save()
    Customer_object.save()
    return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def rent_car(car_id, customer_id):
    try:
        Car_object = Car.objects.get(pk = car_id)
        Customer_object = Customer.objects.get(pk = customer_id) 
        if Car_object.status == 'booked' and Customer_object.customer_status == Car_object: #sjekker at bilen er booket, og at det er kunden som har booket den
            Car_object.status = 'rented'
    except Car_object.DoesNotExist or Customer_object.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    Car_object.save()
    return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def return_car(car_id, customer_id):
    try: 
        Car_object = Car.objects.get(pk = car_id)
        Customer_object = Customer.objects.get(pk = customer_id) 
        if Car_object.status == 'rented' and Car_object.condition == 'ok' and Customer_object.customer_status == Car_object: #sjekker at bilen er utleid og at det er den kunden er den som har leid bilen
            Car_object.status = 'available'
            Customer_object.customer_status = None

        elif Car_object.status == 'rented' and Car_object.condition == 'damaged' and Customer_object.customer_status == Car_object: #sjekker om bilen er skadet, og endrer deretter status til damaged
            Car_object.status = 'damaged'
            Customer_object.customer_status = None
    except Car_object.DoesNotExist or Customer_object.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    Car_object.save()
    Customer_object.save()
    return Response(status = status.HTTP_204_NO_CONTENT)

#Kilde: lecture 8 
#Samarbeidet/fått veiledning av Viktor Klindt til å lage customer_status og bruke OnetoOne.Field (i samme seminargruppe)