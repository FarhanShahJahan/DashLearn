from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

from accounts.models import Account

class RegistrationForm(UserCreationForm):
    matric = forms.CharField(max_length=10, help_text='Required Matric.')


    class Meta:
        model = Account
        fields = ('matric','program', 'password1', 'password2')

class profileForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('password',)
   