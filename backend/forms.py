from django import forms
from .models import Contact

class QabulForm(forms.Form):
    full_name = forms.CharField(label="To'liq ismi", max_length=255)
    passport = forms.CharField(label='Passport seriyasi', max_length=20)
    address = forms.CharField(label='Address', max_length=255)
    phone_number = forms.CharField(label='Telefon raqami', max_length=15)
    directions = forms.CharField(label="Yo'nalish", max_length=100)
    education_type = forms.ChoiceField(
        label="Ta'lim shakli",
        choices=[
            ('full_time', 'Kunduzgi'),
            ('part_time', 'Sirtqi'),
        ]
    )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'phone']