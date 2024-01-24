from app.models import *
from django import forms

class userForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}

class profileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=['image','address']