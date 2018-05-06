from django import forms
from .models import User, Student


# Class UserForm, Use to Create Model User [Objects]
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),           # name field of Class User
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),      # last_name field of Class User
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),   # password field of Class User
            'email': forms.TextInput(attrs={'class': 'form-control'}),          # email field of Class User
            'phone': forms.TextInput(attrs={'class': 'form-control'}),          # phone field of Class User
            'state': forms.TextInput(attrs={'class': 'form-control'}),          # state field of Class User
            'user_type': forms.SelectMultiple(attrs={'class': 'form-control'}), # category field of Class Income
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject_student': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

