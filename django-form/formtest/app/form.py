from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField()
    age = forms.IntegerField()


class MultiForm(forms.Form):
    contacts = forms.formset_factory(ContactForm, extra=3)
