from django.db import models

# Create your models here.

class EmployeeDetails(models.Model):
    Employee_id = models.CharField(max_length=10, null=False, primary_key=True)
    Name = models.CharField(max_length=20, null=False)
    Age = models.IntegerField(null=False)
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    Gender = models.CharField(max_length=20, choices=GENDER, null=False)
    Date_of_birth = models.DateField()
    Father_name = models.CharField(max_length=20, null=False)
    Number = models.CharField(max_length=10, null=False)
    Emergency_no = models.CharField(max_length=10, help_text='Father number or Guardian number')
    Official_email = models.CharField(max_length=20, null=False)  # Corrected field name
    Address = models.TextField(max_length=150, null=False)
    BLOOD_GROUP = [
        ('A+', 'A+'),
        ('A1+', 'A1+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('A1B-', 'A1B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    Blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP, null=False)  # Fixed primary_key attribute
    Employee_role = models.CharField(max_length=20)
    date_of_join = models.DateField()
    Password = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.Name

class Attendance(models.Model):
    Emp_id = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    Date = models.DateField()
    intime = models.TimeField() 
    Lunch = models.TimeField()  
    AfterLunch = models.TimeField() 
    Break = models.TimeField() 
    AfterL_Break = models.TimeField()  
    Leave = models.TimeField()  
    Outtime = models.TimeField()  

    def __str__(self) :
        return str(self.Emp_id)
