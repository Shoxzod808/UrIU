from django import forms
from .models import Contact

class QabulForm(forms.Form):
    full_name = forms.CharField(label="To'liq ismi", max_length=255)
    passport = forms.CharField(label='Passport seriyasi', max_length=20)
    viloyat = forms.CharField(label='Viloyat', max_length=255)
    tuman = forms.CharField(label='Tuman', max_length=255)
    mfy = forms.CharField(label='MFY', max_length=255)
    kucha = forms.CharField(label='Kucha', max_length=255)
    uy = forms.CharField(label='Uy', max_length=255)
    phone_number = forms.CharField(label='Telefon raqami', max_length=15)
    
    birthday = forms.DateField(label="Tug'gilgan kuni", widget=forms.DateInput(attrs={'type': 'date'}))
    school = forms.CharField(label='Tugatgan ta’lim muassasasi', max_length=255)
    attestat = forms.CharField(label="Diplom yoki attestat raqami: № ", max_length=255)
    languages = forms.CharField(label="Qaysi chet til(lar)ini o‘qigan", max_length=255)
    father = forms.CharField(label="Otasi", max_length=255)
    father_address = forms.CharField(label="Doimiy yashash manzili", max_length=255)
    father_job = forms.CharField(label="Doimiy ish joyi", max_length=255)
    father_phone_number = forms.CharField(label="Telefon raqami", max_length=15)
    
    mother = forms.CharField(label="Onasi", max_length=255)
    mother_address = forms.CharField(label="Doimiy yashash manzili", max_length=255)
    mother_job = forms.CharField(label="Doimiy ish joyi", max_length=255)
    mother_phone_number = forms.CharField(label="Telefon raqami", max_length=15)
    directions = forms.ChoiceField(
        label="Yo'nalish", 
        choices=[
        ("Boshlang'ich ta'lim", "Boshlang'ich ta'lim"),
        ("Tarix", "Tarix"),
        ("Filoligiya va tillarni o'qitish(O'zbek tili)", "Filoligiya va tillarni o'qitish(O'zbek tili)"),
        ("Filoligiya va tillarni o'qitish(Ingliz tili)", "Filoligiya va tillarni o'qitish(Ingliz tili)"),
        ],
    )
    education_type = forms.ChoiceField(
        label="Ta'lim shakli",
        choices=[
            ('Kunduzgi', 'Kunduzgi'),
            ('Sirtqi', 'Sirtqi'),
        ]
    )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'phone', 'directions', 'education_type']