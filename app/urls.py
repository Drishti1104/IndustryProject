from django.urls import path
from . import views
# from django.conf.urls import include
from django.urls import path, include
from django_email_verification import urls as email_urls

urlpatterns = [
    path('', views.index, name='index'),
    path('inner-page/', views.inner_page, name='inner-page'),
    path('index-login/', views.index_login, name='index-login'),
    path('index-dr/', views.index_dr, name='index-dr'),
    path('sample/', views.sample, name='sample'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('screening/', views.screening, name='screening'),
    path('screening-dr/', views.screening_dr, name='screening-dr'),
    path('screening-data/', views.screening_data, name='screening-data'),
    path('appointment-data/', views.appointment_data, name='appointment-data'),
    path('screening-questions/', views.screening_questions, name='screening-questions'),
    path('screening-qn-2/', views.screening_qn_2, name='screening-qn-2'),
    path('about-us/', views.about_us, name='about-us'),
    path('profile-details/', views.profile_details, name='profile-details'),
    path('wait/', views.wait, name='wait'),
    path('result/', views.result, name='result'),
    path('appointment/', views.appointment, name='appointment'),
    path('confirmemail/', views.confirmemail, name="confirmemail"),
    path('doctor-details/', views.doctor_details, name="doctor-details"),
    path('index-intern/', views.index_intern, name="index-intern"),
    path('screening-intern/', views.screening_intern, name="screening-intern"),
    path('trackappointment/', views.trackappointment, name="trackappointment"),
    path('screening-data-intern/', views.screening_data_intern, name="screening-data-intern"),
    path('generate-report/', views.generate_report, name="generate-report"),
    path('generate-report-pk/<int:pk>/', views.generate, name="generate-report-pk"),
    path('reschedule', views.reschedule, name="reschedule"),
    path('depression-questions', views.depression_questions, name="depression-questions"),
    path('verifyotppage', views.verifyotppage, name="verifyotppage"),
    path('verifyotp', views.verifyotp, name="verifyotp"),
    # path("blog/", include(("blog.urls", "blog"), namespace = "blog")),
]