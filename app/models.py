from datetime import datetime

from django.db import models
# from pytz import timezone
from sqlalchemy import Time
from datetime import date

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=100, default="your name")
    email = models.EmailField(max_length=50)
    dob = models.DateField(default=datetime.now())
    contact = models.CharField(max_length=10, default="1234567890")
    job = models.CharField(max_length=50, default="job")
    gender = models.CharField(max_length=20, default="gender")
    password = models.CharField(max_length=25)
    cPassword = models.CharField(max_length=25)
    date = models.DateTimeField()
    isUser = models.CharField(max_length=30, default="user")
    isactive = models.BooleanField(default = False)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.email
    

class ScreeningTest(models.Model):
    email = models.EmailField(max_length=50, default="email")
    nature_of_concern = models.CharField(max_length=500, null=True)
    otherReason = models.TextField(max_length=300, null=True)
    physicalFitness = models.CharField(max_length=10, default="5", null=True)
    stress = models.CharField(max_length=10, default="5", null=True)
    help = models.CharField(max_length=25, default="Moderate", null=True)
    psychologist = models.CharField(max_length=500,default="Default", null=True)
    doctor = models.CharField(max_length=200, default="Default", null=True)
    isactive = models.BooleanField(default = False)
    def __str__(self):
        return self.email

# class ScreeningQn(models.Model):
#     email = models.EmailField(max_length=50, default="email")
#     physicalFitness = models.CharField(max_length=10, default="5", null=True)
#     stress = models.CharField(max_length=10, default="5", null=True)
#     help = models.CharField(max_length=25, default="Moderate", null=True)
#     def __str__(self):
#         return self.email
        
class Appointment(models.Model):
    fname = models.CharField(max_length=100, default="first name")
    lname = models.CharField(max_length=100, default="last name")
    email = models.EmailField(max_length=50)
    # contact = models.CharField(max_length=10, default="1234567890")
    doa = models.DateField(default=datetime.now())
    time = models.TimeField(default=Time)
    message = models.TextField(max_length=200, default="message")
    mode = models.CharField(max_length=20, default="offline")
    doctor = models.CharField(max_length=20, default="any")
    isactive = models.BooleanField(default = False)

    def __str__(self):
        return self.email

class Doctor(models.Model):
    fname = models.CharField(max_length=100, default="first name")
    lname = models.CharField(max_length=100, default="last name")
    image = models.ImageField(upload_to="doctor", null=True)
    qualification = models.TextField(max_length=200, default="qualification")
    description = models.TextField(max_length=200, default="desc")

    def __str__(self):
        return self.fname

class Reschedule(models.Model):
    doa = models.DateField(default=datetime.now())
    time = models.TimeField(default=Time)
    mode = models.CharField(max_length=20, default="offline")
    # doctor = models.CharField(max_length=20, default="any")
    isactive = models.BooleanField(default = False)

class DepressionTest(models.Model):
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()
    score = models.IntegerField(default=0)
    user = models.ForeignKey(Register, on_delete=models.SET_NULL, null=True)
    age = models.IntegerField(null=True)