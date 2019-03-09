from django import forms
from django.contrib.auth.models import User
from examapp2.models import UserProfileInfo
from examapp2.models import TotalScore

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields = ['role']

class TotalScoreForm(forms.ModelForm):
    class Meta:
        model = TotalScore
        fields='__all__'
