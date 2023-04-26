from datetime import datetime, date
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt 
from django.conf import settings
from django.http import HttpResponse

from django.core.exceptions import MultipleObjectsReturned
from django_zoom_meetings import ZoomMeetings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

import random
import json
import joblib, pickle
import numpy as np

from .model import Model
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def index_login(request):
    return render(request, 'app/index-login.html')

def index_dr(request):
    return render(request, 'app/index-dr.html')

def inner_page(request):
    return render(request, 'app/inner-page.html')

def sample(request):
    return render(request, 'app/sample.html')

def screening(request):
    return render(request, 'app/screening.html')

def about_us(request):
    return render(request, 'app/about-us.html')

def profile_details(request):
    return render(request, 'app/profile-details.html')

def wait(request):
    return render(request, 'app/wait.html')

def screening_dr(request):
    return render(request, 'app/screening-dr.html')

def screening_data(request):
    data1 = ScreeningTest.objects.all()
    return render(request, 'app/screening-data.html', {'data1':data1})

def appointment_data(request):
    data = Appointment.objects.all()
    return render(request, 'app/appointment-data.html', {'data':data})

def verifyotppage(request):
    return render(request, 'app/verify-otp-page.html')

def doctor_details(request):
    doctor = Doctor.objects.all()
    return render(request, 'app/doctor-details.html', {'doctor': doctor})

def index_intern(request):
    return render(request, 'app/index-intern.html')

def screening_intern(request):
    return render(request, 'app/screening-intern.html')

def generate_report(request):
    if request.method=="POST":
        recipient_list = request.POST['email']
        doctor = request.POST['doctor']

    report = ScreeningTest.objects.get(email=recipient_list)
    report.doctor = doctor
    report.save(update_fields=['doctor'])

    html_content = render_to_string("app/report.html", {'report': report})
    text_content = strip_tags(html_content)
    email_from = settings.EMAIL_HOST_USER

    email = EmailMultiAlternatives(
        "Mental Wellness - Mind Matters", #subject
        text_content, #content
        email_from, #from_email
        [recipient_list] #to email
    )
    email.attach_alternative(html_content, "text/html")
    email.send()
    messages.success(request, "Report emailed successfully")
    return redirect('screening-data-intern')


def generate(request, pk):
    report = ScreeningTest.objects.get(id=pk)
    return render(request, 'app/generate-report.html', {'report': report})

def screening_data_intern(request):
    data1 = ScreeningTest.objects.all()
    return render(request, 'app/screening-data-intern.html', {'data1':data1})

def userLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        fnd = Register.objects.filter(email=email)
        if len(fnd) > 0:
            if fnd[0].password == password:
                request.session['id'] = fnd[0].id
                request.session['email'] = fnd[0].email
                request.session['isUser'] = fnd[0].isUser
                request.session['isactive']=fnd[0].isactive
                if 'isUser' in request.session:
                    print("yes")
                    if request.session['isactive'] == True:
                        # if request.session['isUser'] == 'doctor':
                        #     messages.success(request, "Login Successful")
                        #     return redirect('index-dr')
                        # if request.session['isUser'] == 'intern':
                        #     messages.success(request, "Login Successful")
                        #     return redirect('index-intern')
                        messages.success(request, "Login Successful")
                        return redirect('index')
                    else:
                        messages.error(request, "Please verify your account using the link sent on your mail")
                        return redirect('login')
                
            else:
                messages.error(request, "Username or Password is incorrect")
                return redirect('login')
        else:
            messages.success(request, "User does not exist. Please register.")
            return redirect("register")
            
    return render(request, 'app/login.html')

def logout(request):
    del request.session['id']
    del request.session['email']
    del request.session['isUser']
    if 'isUser' not in request.session:
        print("no")
    return redirect('index')

def screening_questions(request):
    if request.method=="POST":
        request.session['concern_list'] = request.POST.getlist('concern')
        # request.session['otherReason'] = request.POST.get('otherReason')
        if 'concern_list' in request.session:
            print(request.session['concern_list'])
        if request.session['concern_list']:
            return redirect('screening-qn-2')
    return render(request, "app/screening-questions.html")

def screening_qn_2(request):
    if request.method=="POST":
        physicalFitness = request.POST.get('PhysicalFitness')
        stress = request.POST.get('Stress')
        help = request.POST.get('Help')
        screening = ScreeningTest(
            nature_of_concern = request.session['concern_list'],
            # otherReason = request.session['otherReason'],
            physicalFitness = physicalFitness,
            stress = stress,
            help = help,
            email = request.session['email']
        )
        screening.save()
        psy = []
        nature_of_concern = request.session['concern_list']
        noc = list(nature_of_concern)
        print(nature_of_concern)
        n = ScreeningTest.objects.all().filter(nature_of_concern = request.session['concern_list']).count()
        for i in nature_of_concern:
            if i =='Professional':
                psy.append('Industrial')
            elif i =='Emotional':
                psy.append('Clinical')
            elif i =='Relationship':
                psy.append('Counselling')
            elif i =='Motivation':
                psy.append('Clinical')
                psy.append('Sports')
            elif i =='Sleep':
                psy.append('Clinical')
            elif i =='Performance':
                psy.append('Industrial')
                psy.append('Sports')
            elif i =='Focus':
                psy.append('Clinical')
                psy.append('Sports')
            elif i =='Family':
                psy.append('Counselling')
            elif i =='PhysicalChange':
                psy.append('Clinical')
                psy.append('Sports')
            elif i =='Trauma':
                psy.append('Clinical')
            elif i =='Self':
                psy.append('Counselling')
                psy.append('Clinical')
                psy.append('Sports')
            elif i =='Substance':
                psy.append('Clinical')
            elif i =='Abuse':
                psy.append('Clinical')
            elif i =='Suicidal':
                psy.append('Clinical')
            elif i =='Compulsive':
                psy.append('Clinical')
            elif i =='Adjust':
                psy.append('Counselling')
                psy.append('Clinical')
            elif i =='Lonely':
                psy.append('Counselling')
                psy.append('Clinical')
            elif i =='GenderIdentity':
                psy.append('Counselling')
                psy.append('Clinical')
            elif i =='Appitite':
                psy.append('Clinical')
                psy.append('Sports')
            elif i =='Bully':
                psy.append('Clinical')
                psy.append('Child')
                psy.append('Counselling')
            elif i =='WorkPlace':
                psy.append('Sports')
                psy.append('Industrial')
            elif i =='PerformanceBurnOut':
                psy.append('Sports')
            elif i =='Rehab':
                psy.append('Sports')
            elif i =='Development':
                psy.append('Clinical')
                psy.append('Child')
            elif i =='AnimalAbuse':
                psy.append('Clinical')
            elif i =='ImpulseControl':
                psy.append('Sports')
                psy.append('Industrial')
                psy.append('Clinical')
            elif i =='Psychotic':
                psy.append('Clinical')
            elif i =='Anger':
                psy.append('Clinical')
                psy.append('Counselling')
            elif i =='Sibiling':
                psy.append('Counselling')
                psy.append('Child')
            elif i =='BrainFog':
                psy.append('Sports')
                psy.append('Industrial')
                psy.append('Clinical')
                psy.append('Counselling')
            elif i =='NegativePeer':
                psy.append('Sports')
                psy.append('Industrial')
        ls=set(psy)
        lis=list(ls)
        screening.psychologist=lis
        screening.save(update_fields=['psychologist'])
        return redirect('wait')
    return render(request, "app/screening_qn_2.html")

def result(request):
    # global nature_of_concern 
    # professional = 0
    # nature = ScreeningTest.objects.values_list('nature_of_concern')
    # # print(nature)
    # for list1 in nature:
    #     for list2 in list1:
    #         for list3 in list2:
    #             if 'Professional' in list3:
    #                 professional += 1
    # print(list1)
    # print(list2)
    # print(list3)
    # print(professional)
    
        age20 = DepressionTest.objects.all().filter(age__gte=18, age__lte=24).count()
        print(age20)
        q1_0_18 = DepressionTest.objects.all().filter(q1=0, age__gte=18, age__lte=24).count()
        q1_1_18 = DepressionTest.objects.all().filter(q1=1, age__gte=18, age__lte=24).count()
        q1_2_18 = DepressionTest.objects.all().filter(q1=2, age__gte=18, age__lte=24).count()
        q1_3_18 = DepressionTest.objects.all().filter(q1=3, age__gte=18, age__lte=24).count()

        q1_0_25 = DepressionTest.objects.all().filter(q1=0, age__gte=25, age__lte=39).count()
        q1_1_25 = DepressionTest.objects.all().filter(q1=1, age__gte=25, age__lte=39).count()
        q1_2_25 = DepressionTest.objects.all().filter(q1=2, age__gte=25, age__lte=39).count()
        q1_3_25 = DepressionTest.objects.all().filter(q1=3, age__gte=25, age__lte=39).count()

        q1_0_40 = DepressionTest.objects.all().filter(q1=0, age__gte=40).count()
        q1_1_40 = DepressionTest.objects.all().filter(q1=1, age__gte=40).count()
        q1_2_40 = DepressionTest.objects.all().filter(q1=2, age__gte=40).count()
        q1_3_40 = DepressionTest.objects.all().filter(q1=3, age__gte=40).count()

        q5_0_18 = DepressionTest.objects.all().filter(q5=0, age__gte=18, age__lte=24).count()
        q5_1_18 = DepressionTest.objects.all().filter(q5=1, age__gte=18, age__lte=24).count()
        q5_2_18 = DepressionTest.objects.all().filter(q5=2, age__gte=18, age__lte=24).count()
        q5_3_18 = DepressionTest.objects.all().filter(q5=3, age__gte=18, age__lte=24).count()
        
        q5_0_25 = DepressionTest.objects.all().filter(q5=0, age__gte=25, age__lte=39).count()
        q5_1_25 = DepressionTest.objects.all().filter(q5=1, age__gte=25, age__lte=39).count()
        q5_2_25 = DepressionTest.objects.all().filter(q5=2, age__gte=25, age__lte=39).count()
        q5_3_25 = DepressionTest.objects.all().filter(q5=3, age__gte=25, age__lte=39).count()

        q5_0_40 = DepressionTest.objects.all().filter(q5=0, age__gte=40).count()
        q5_1_40 = DepressionTest.objects.all().filter(q5=1, age__gte=40).count()
        q5_2_40 = DepressionTest.objects.all().filter(q5=2, age__gte=40).count()
        q5_3_40 = DepressionTest.objects.all().filter(q5=3, age__gte=40).count()

        q7_0_18 = DepressionTest.objects.all().filter(q7=0, age__gte=18, age__lte=24).count()
        q7_1_18 = DepressionTest.objects.all().filter(q7=1, age__gte=18, age__lte=24).count()
        q7_2_18 = DepressionTest.objects.all().filter(q7=2, age__gte=18, age__lte=24).count()
        q7_3_18 = DepressionTest.objects.all().filter(q7=3, age__gte=18, age__lte=24).count()
        
        q7_0_25 = DepressionTest.objects.all().filter(q7=0, age__gte=25, age__lte=39).count()
        q7_1_25 = DepressionTest.objects.all().filter(q7=1, age__gte=25, age__lte=39).count()
        q7_2_25 = DepressionTest.objects.all().filter(q7=2, age__gte=25, age__lte=39).count()
        q7_3_25 = DepressionTest.objects.all().filter(q7=3, age__gte=25, age__lte=39).count()

        q7_0_40 = DepressionTest.objects.all().filter(q7=0, age__gte=40).count()
        q7_1_40 = DepressionTest.objects.all().filter(q7=1, age__gte=40).count()
        q7_2_40 = DepressionTest.objects.all().filter(q7=2, age__gte=40).count()
        q7_3_40 = DepressionTest.objects.all().filter(q7=3, age__gte=40).count()

        q9_0_18 = DepressionTest.objects.all().filter(q9=0, age__gte=18, age__lte=24).count()
        q9_1_18 = DepressionTest.objects.all().filter(q9=1, age__gte=18, age__lte=24).count()
        q9_2_18 = DepressionTest.objects.all().filter(q9=2, age__gte=18, age__lte=24).count()
        q9_3_18 = DepressionTest.objects.all().filter(q9=3, age__gte=18, age__lte=24).count()
        
        q9_0_25 = DepressionTest.objects.all().filter(q9=0, age__gte=25, age__lte=39).count()
        q9_1_25 = DepressionTest.objects.all().filter(q9=1, age__gte=25, age__lte=39).count()
        q9_2_25 = DepressionTest.objects.all().filter(q9=2, age__gte=25, age__lte=39).count()
        q9_3_25 = DepressionTest.objects.all().filter(q9=3, age__gte=25, age__lte=39).count()

        q9_0_40 = DepressionTest.objects.all().filter(q9=0, age__gte=40).count()
        q9_1_40 = DepressionTest.objects.all().filter(q9=1, age__gte=40).count()
        q9_2_40 = DepressionTest.objects.all().filter(q9=2, age__gte=40).count()
        q9_3_40 = DepressionTest.objects.all().filter(q9=3, age__gte=40).count()

        return render(request, 'app/result.html', {
            'q1_0_18': q1_0_18, 
            'q1_1_18': q1_1_18, 
            'q1_2_18': q1_2_18, 
            'q1_3_18': q1_3_18,

            'q1_0_25': q1_0_25, 
            'q1_1_25': q1_1_25, 
            'q1_2_25': q1_2_25, 
            'q1_3_25': q1_3_25,

            'q1_0_40': q1_0_40, 
            'q1_1_40': q1_1_40, 
            'q1_2_40': q1_2_40, 
            'q1_3_40': q1_3_40,

            'q5_0_18': q5_0_18, 
            'q5_1_18': q5_1_18, 
            'q5_2_18': q5_2_18, 
            'q5_3_18': q5_3_18,

            'q5_0_25': q5_0_25, 
            'q5_1_25': q5_1_25, 
            'q5_2_25': q5_2_25, 
            'q5_3_25': q5_3_25,

            'q5_0_40': q5_0_40, 
            'q5_1_40': q5_1_40, 
            'q5_2_40': q5_2_40, 
            'q5_3_40': q5_3_40,

            'q7_0_18': q7_0_18, 
            'q7_1_18': q7_1_18, 
            'q7_2_18': q7_2_18, 
            'q7_3_18': q7_3_18,

            'q7_0_25': q7_0_25, 
            'q7_1_25': q7_1_25, 
            'q7_2_25': q7_2_25, 
            'q7_3_25': q7_3_25,

            'q7_0_40': q7_0_40, 
            'q7_1_40': q7_1_40, 
            'q7_2_40': q7_2_40, 
            'q7_3_40': q7_3_40,

            'q9_0_18': q9_0_18, 
            'q9_1_18': q9_1_18, 
            'q9_2_18': q9_2_18, 
            'q9_3_18': q9_3_18,

            'q9_0_25': q9_0_25, 
            'q9_1_25': q9_1_25, 
            'q9_2_25': q9_2_25, 
            'q9_3_25': q9_3_25,

            'q9_0_40': q9_0_40, 
            'q9_1_40': q9_1_40, 
            'q9_2_40': q9_2_40, 
            'q9_3_40': q9_3_40,
 
        })

class Result(TemplateView):
    model = ScreeningTest
    template_name = 'app/result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = ScreeningTest.objects.all()
        return context

def appointment(request):
    # screening = ScreeningTest.objects.get(email=request.session['email'])
    # print(screening)
    # if screening == 0:
    #     messages.success(request, "Please take the screening test first.")
    #     return redirect('screening')
        
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.session['email']
        doa = request.POST.get('doa')
        # contact = request.POST.get('contact')
        mode = request.POST.get('mode')
        dr = request.POST.get('dr')
        message = request.POST.get('message')
        time = request.POST.get('time')

        appointment = Appointment(
            fname=fname,
            lname=lname,
            email=email,
            doa=doa,
            # contact=contact,
            mode=mode,
            doctor=dr,
            message=message,
            time=time
        )
        my_zoom = ZoomMeetings('kK3rbkG1SVuUz3Q2ygX1sA','jBZS2owwH750Rm9i35zxZyi6N7dDFlunew25','mental.wellness.mind.matters@gmail.com')
        
        # print(create_meeting['join_url'])
        try:
            data = Appointment.objects.get(email= request.session['email'])
            if data:
                messages.error(request, 'You have an already scheduled appointment!')

        except:
            appointment.isactive=True
            appointment.save()
            cr_date = str(appointment.doa)+" "+str(appointment.time)+":00"+'.000227'
            cr_date = datetime.strptime(cr_date, '%Y-%m-%d %H:%M:%S.%f')
            create_meeting = my_zoom.CreateMeeting(cr_date,'appointment','40','f4c68')
            if(appointment.mode=='Offline'):
                send_mail(
                'Appointment confirmed',
                    'Congratulations ' + str(fname) +' '+ str(lname) +'. Your appointment is scheduled on '+str(doa)+' at '+str(time)+' with Psychiatrist Shaneela Gharat.' + ' Your Appointment mode is '+str(mode)+ '. All the further details will be provided by Psychiatrist via mail.',
                    'mental.wellness.mind.matters@gmail.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request,'You have successfully booked an appointment!')
            else:
                send_mail(
                'Appointment confirmed',
                    'Congratulations ' + str(fname) +' '+ str(lname) +'. Your appointment is scheduled on '+str(doa)+' at '+str(time)+' with Psychiatrist Shaneela Gharat.' + ' Your Appointment mode is '+str(mode)+ '. All the further details will be provided by Psychiatrist via mail.'+ 'Your meeting link is: '+ create_meeting['join_url'],
                    'mental.wellness.mind.matters@gmail.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request,'You have successfully booked an appointment!')
        return redirect('index-login')
    return render(request, 'app/appointment.html')

@csrf_exempt

def register(request):
    if request.method == "POST":
        existingEmail = Register.objects.filter(email=request.POST.get('email'))
        if len(existingEmail) == 0:
            name = request.POST.get('name')
            email = request.POST.get('email')
            request.session['email'] = email
            dob = request.POST.get('dob')
            contact = request.POST.get('contact')
            job = request.POST.get('job')
            gender = request.POST.get('gender')
            password = request.POST.get('password')
            cPassword = request.POST.get('cPassword')
            if password != cPassword:
                messages.error(request, "Both Passwords do not match")
                return redirect('register')

            register = Register(
                name=name,
                email=email,
                dob=dob,
                contact=contact,
                job=job,
                gender=gender,
                password=password,
                cPassword=cPassword,
                date = datetime.today(),
            )
            # user = User.objects.create_user(username=email, email=email)
            # user.set_password(password)
            # # user = Register.objects
            # user.is_active = False
            
            # send_mail(
            # 'Activate account',
            #     'Please Click http://127.0.0.1:8000/confirmemail to confirm your account',
            #     'mental.wellness.mind.matters@gmail.com',
            #     [email],
            #     fail_silently=False,
            # )
            # user.save()
            request.session['otp'] = random.randint(1000,9999)
            send_otp_email(request.session['otp'], request.session['email'])
            register.save()
            messages.success(request, "OTP is sent to your email. Please enter it.")
            return redirect("verifyotppage")
            # messages.success(request, 'Please check your email to verify your account')
            # return redirect('login')
            # request.session['register']= register
        else:
            messages.success(request, "User already exists. Please login")
            return redirect('login')
    return render(request, 'app/register.html')

def send_otp_email(otp, email):
    subject = "Verify your Email - {}".format(email)
    print(otp)
    message = "Your 4-digit OTP to verify your account is : " + str(otp) + ". Please don't share it with anyone else"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

# def send_psw_email(otp, email):
#     subject = "Reset your Password - {}".format(email)
#     print(otp)
#     message = "Your 4-digit OTP to reset your password is : " + str(otp) + ". Please don't share it with anyone else"
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject, message, email_from, recipient_list)

def confirmemail(request):
    # register = request.session['register']
    register = Register.objects.get(email= request.session['email'])
    today = date.today()
    age = today.year - register.dob.year - ((today.month, today.day) < (register.dob.month, register.dob.day))
    print(age)
    register.isactive=True
    register.age = age
    register.save(update_fields=['isactive', 'age'])
    return HttpResponse('You have registered successfully! Please click http://127.0.0.1:8000/login to login')

def verifyotp(request):
    if request.method == "POST":
        mainotp = request.POST['otp']
        print(type(mainotp), type(request.session['otp']))
        if request.session['otp'] == int(mainotp):
            register = Register.objects.get(email= request.session['email'])
            today = date.today()
            age = today.year - register.dob.year - ((today.month, today.day) < (register.dob.month, register.dob.day))
            print(age)
            request.session['age'] = age
            register.isactive=True
            register.age = age
            register.save(update_fields=['isactive', 'age'])
            messages.success(request, "You have Registered successfully. Login to continue.")
            return redirect("login")
        else:
            messages.error(request, "Invalid OTP. Please try again")
            return redirect("verifyotppage")

def trackappointment(request):
    if Appointment.objects.filter(email= request.session['email']).exists():
        try:
            data = Appointment.objects.get(email= request.session['email'])
            return render(request, 'app/trackappointment.html',{'data':data})
        except MultipleObjectsReturned:
            data=Appointment.objects.filter(email= request.session['email']).first()
            return render(request, 'app/trackappointment.html',{'data':data})
    else:
        messages.success(request, "Please schedule an appointment first")
        return redirect('doctor-details')
    

def reschedule(request):
    if request.method == "POST":
        doa = request.POST.get('doa')
        email=request.session['email']
        # contact = request.POST.get('contact')
        mode = request.POST.get('mode')
        # dr = request.POST.get('dr')
        time = request.POST.get('time')
        reschedule = Reschedule(
            doa=doa,
            mode=mode,
            # doctor=dr,
            time=time
        )

        appointment = Appointment.objects.get(email=request.session['email'])
        if appointment.isactive==True:
            appointment.doa=doa
            appointment.time=time
            appointment.mode=mode
            appointment.save(update_fields=['doa','mode','time'])
            # appointment.save(update_fields=['mode'])
            # appointment.save(update_fields=['time'])
            my_zoom = ZoomMeetings('kK3rbkG1SVuUz3Q2ygX1sA','jBZS2owwH750Rm9i35zxZyi6N7dDFlunew25','mental.wellness.mind.matters@gmail.com')
            cr_date = str(appointment.doa)+" "+str(appointment.time)+":00"+'.000227'
            cr_date = datetime.strptime(cr_date, '%Y-%m-%d %H:%M:%S.%f')
            create_meeting = my_zoom.CreateMeeting(cr_date,'appointment','40','f4c68')
            if(appointment.mode=='Offline'):
                
                send_mail(
                'Appointment Rescheduled',
                    'Congratulations ' + str(appointment.fname) +' '+ str(appointment.lname) +'. Your appointment is scheduled on '+str(doa)+' at '+str(time)+' with Psychiatrist Shaneela Gharat.' + ' Your Appointment mode is '+str(mode)+ '. All the further details will be provided by Psychiatrist via mail.',
                    'mental.wellness.mind.matters@gmail.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request,'You have successfully booked an appointment!')
            else:
                send_mail(
                'Appointment confirmed',
                    'Congratulations ' + str(appointment.fname) +' '+ str(appointment.lname) +'. Your appointment is scheduled on '+str(doa)+' at '+str(time)+' with Psychiatrist Shaneela Gharat.' + ' Your Appointment mode is '+str(mode)+ '. All the further details will be provided by Psychiatrist via mail.'+ 'Your meeting link is: '+ create_meeting['join_url'],
                    'mental.wellness.mind.matters@gmail.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request,'You have successfully booked an appointment!')
        return redirect('trackappointment')
    return render(request, 'app/reschedule.html')

def depression_questions(request):
    score = 0
    if request.method=="POST":
        q1 = int(request.POST.get('q1'))
        q2 = int(request.POST.get('q2'))
        q3 = int(request.POST.get('q3'))
        q4 = int(request.POST.get('q4'))
        q5 = int(request.POST.get('q5'))
        q6 = int(request.POST.get('q6'))
        q7 = int(request.POST.get('q7'))
        q8 = int(request.POST.get('q8'))
        q9 = int(request.POST.get('q9'))
        q10 = int(request.POST.get('q10'))
        score = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10
        user = Register.objects.get(email=request.session['email'])
        age = user.age
        print(score)
        depression = DepressionTest(
            q1 = q1,
            q2 = q2,
            q3 = q3,
            q4 = q4,
            q5 = q5,
            q6 = q6,
            q7 = q7,
            q8 = q8,
            q9 = q9,
            q10 = q10,
            score = score,
            user = user,
            age = age,
        )
        depression.save()
        values = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
        model = Model()
        classifier = model.naiveBayes_classifier()
        prediction = classifier.predict([values])
        if prediction[0] == 0:
                result = 'Your Depression test result : No Depression'
        if prediction[0] == 1:
                result = 'Your Depression test result : Mild Depression'
        if prediction[0] == 2:
                result = 'Your Depression test result : Moderate Depression'
        if prediction[0] == 3:
                result = 'Your Depression test result : Moderately severe Depression'
        if prediction[0] == 4:
                result = 'Your Depression test result : Severe Depression'
        return render(request, "app/depression-result.html",{'ans':result})
    return render(request, 'app/depression-questions.html')


# def report(request):
#     ScreeningTest = ScreeningTest.objects.get(email= request.session['email'])

# def createmeeting(request):
#     my_zoom = ZoomMeetings(api_key,secret_key,zoom_email)
#     create_meeting = my_zoom.CreateMeeting(date,str_topic,str_meeting_duration,str_meeting_password)