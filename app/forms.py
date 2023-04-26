# from turtle import title
# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
 
# # class UserRegisterForm(UserCreationForm):
# #     email = forms.EmailField()
# #     phone_no = forms.CharField(max_length = 20)
# #     first_name = forms.CharField(max_length = 20)
# #     last_name = forms.CharField(max_length = 20)
# #     class Meta:
# #         model = User
# #         fields = ['username', 'email', 'phone_no', 'password1', 'password2']

# q1_choices = [
#     ('Excellent', 'Excellent'),
#     ('Good', 'Good'),
#     ('Average', 'Average'),
#     ('Poor', 'Poor'),
# ]

# q2_choices = [
#     ('Excellent', 'Excellent'),
#     ('Good', 'Good'),
#     ('Average', 'Average'),
#     ('Poor', 'Poor'),
# ]

# q3_choices = [
#     ('Yes', 'Yes'),
#     ('No', 'No'),
#     ('Not Sure', 'Not sure'),
# ]

# q4_choices = [
#     ('Yes', 'Yes'),
#     ('No', 'No'),
#     ('Not Sure', 'Not sure'),
# ]

# q5_choices = [
#     ('Very Often', 'Very often'),
#     ('Somewhat often', 'Somewhat often'),
#     ('Not so often', 'Not so often'),
#     ('Not at all', 'Not at all'),
# ]

# q6_choices = [
#     ('Very Often', 'Very often'),
#     ('Somewhat often', 'Somewhat often'),
#     ('Not so often', 'Not so often'),
#     ('Not at all', 'Not at all'),
# ]

# q7_choices = [
#     ('Yes', 'Yes'),
#     ('No', 'No'),
#     ('Not Sure', 'Not sure'),
# ]

# q8_choices = [
#     ('Never', 'Never'),
#     ('Once in a week', 'Once in a week'),
#     ('Once everyday', 'Once everyday'),
#     ('More than once everyday', 'More than once everyday'),
# ]

# q9_choices = [
#     ('Never', 'Never'),
#     ('Once in a week', 'Once in a week'),
#     ('Once everyday', 'Once everyday'),
#     ('More than once everyday', 'More than once everyday'),
# ]

# q10_choices = [
#     ('Single', 'Single'),
#     ('Married', 'Married'),
#     ('Divorced', 'Divorced'),
#     ('Widowed', 'Widowed'),
#     ('Separated', 'Separated'),
# ]

# q11_choices = [
#     ('Less than 5', 'Less than 5'),
#     ('5 to 7', '5 to 7'),
#     ('7 to 9', '7 to 9'),
#     ('More than 9', 'More than 9'),
# ]

# q12_choices = [
#     ('Yes', 'Yes'),
#     ('No', 'No'),
#     ('In progress', 'In progress'),
#     ('Not applicable', 'Not applicable'),
# ]

# q13_choices = [
#     ('Very Often', 'Very often'),
#     ('Somewhat often', 'Somewhat often'),
#     ('Not so often', 'Not so often'),
#     ('Not at all', 'Not at all'),
# ]

# class ScreeningForm(forms.Form):
#     q1 = forms.CharField(label="Q1. Overall how would you rate your physical health?", widget=forms.RadioSelect(choices=q1_choices))
#     q2 = forms.CharField(label="Q2. How would you rank your mental wellness all around?", widget=forms.RadioSelect(choices=q2_choices))
#     q3 = forms.CharField(label="Q3. Has your physical health caused you any issues at work or in your daily life over the last four weeks?", widget=forms.RadioSelect(choices=q3_choices))
#     q4 = forms.CharField(label="Q4. During the past 4 weeks, have you had any problems with your work or daily life due to any emotional problems, such as feeling depressed, sad or anxious?", widget=forms.RadioSelect(choices=q4_choices))
#     q5 = forms.CharField(label="Q5. How often has your mental health affected your ability to get work done?", widget=forms.RadioSelect(choices=q5_choices))
#     q6 = forms.CharField(label="Q6. Have you felt particularly low or down for more than 2 weeks in a row?", widget=forms.RadioSelect(choices=q6_choices))
#     q7 = forms.CharField(label="Q7. Are you going through a tough emotional situation?", widget=forms.RadioSelect(choices=q7_choices))
#     q8 = forms.CharField(label="Q8. How often do you smoke?", widget=forms.RadioSelect(choices=q8_choices))
#     q9 = forms.CharField(label="Q9. How often do you drink?", widget=forms.RadioSelect(choices=q9_choices))
#     q10 = forms.CharField(label="Q10. What is your relationship status?", widget=forms.RadioSelect(choices=q10_choices))
#     q11 = forms.CharField(label="Q11. How many hours do you sleep per day?", widget=forms.RadioSelect(choices=q11_choices))
#     q12 = forms.CharField(label="Q12. Have you changed your job recently?", widget=forms.RadioSelect(choices=q12_choices))
#     q13 = forms.CharField(label="Q13. Do you do any physical activity other than normal travelling?", widget=forms.RadioSelect(choices=q13_choices))
#     # email = forms.EmailField(label="Enter your email")


