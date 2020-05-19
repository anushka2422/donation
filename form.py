from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import donation

class donationCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = donation
        fields = ('first_name', 'last_name', 'email', 'EMAIL_ME_A_RECEIPT', 'GIVE_ANONYMOUSLY', 'ADD_ME_TO_EMAIL_LIST')


class donationChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        model = donation
        fields = ('first_name', 'last_name', 'email', 'EMAIL_ME_A_RECEIPT', 'GIVE_ANONYMOUSLY', 'ADD_ME_TO_EMAIL_LIST')


