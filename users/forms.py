from django import forms
from django.contrib.auth.models import User

# signup form
class SignupForm(forms.Form):
    username=forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        username=cleaned_data.get('username')
        email=cleaned_data.get('email')
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password!=confirm_password:
            raise forms.ValidationError("Password Do Not match")
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already Existes!")
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Already exists!")
        

# login form 

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)


# change password form 

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data =  super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')

        if new_password != confirm_new_password:
            raise forms.ValidationError("New Password does Not Match")