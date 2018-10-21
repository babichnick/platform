from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=120, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)