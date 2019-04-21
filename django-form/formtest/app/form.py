from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField()
    age = forms.IntegerField()
