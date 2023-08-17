from django.shortcuts import render,redirect
from . models import EmployeeDetails
from django.contrib import messages

# Create your views here.

def login(request):
    return render(request,'login.html')

def home(request):
    if request.method == 'POST':
        employeeid = request.POST['employeeid']
        employeepassword = request.POST['employeepassword']

    

        mydata = EmployeeDetails.objects.all()
        for data in mydata:
            if data.Employee_id == employeeid:
                if data.Password == employeepassword:
                    return render(request,'home.html')         
        messages.error(request, "Username or password is worng...!") 
    return redirect('login')
            
        


        