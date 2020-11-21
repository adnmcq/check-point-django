# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=0, widget=forms.EmailInput(attrs={'class':'form-control'}))
    subject = forms.CharField(required=0, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), required=0)
    name = forms.CharField(required=0, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(required=0, widget=forms.TextInput(attrs={'class':'form-control'}))