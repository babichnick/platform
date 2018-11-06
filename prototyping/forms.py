from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=120, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )