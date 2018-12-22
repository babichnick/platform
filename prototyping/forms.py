from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=120, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
    captcha = ReCaptchaField()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'password1','password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = user.email
    
        if commit:
            user.save()
        return user