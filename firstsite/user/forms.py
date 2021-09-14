from django.forms import DateInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=225,
    widget = forms.TextInput(
        attrs={
            "placeholder": "Ваше имя...",
            "class": "form-control"
        }
    ))

    last_name = forms.CharField(max_length=225,
        widget = forms.TextInput(
            attrs={
                "placeholder": "Ваша фамилия...",
                "class": "form-control"
            }
    ))
    email = forms.EmailField()


    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'birthday', 'gender', 'phone', 'address', 'number', 'city']
        exclude = ['user']
        widgets = {
            "birthday": DateInput(attrs={
                'class': 'form-control',
                'id': 'birthday',
                'placeholder': 'dd/mm/yyyy'
            }),
            "gender": DateInput(attrs={
                'class': 'form-control',
                'id': 'gender',
                'placeholder': 'Выберите ваш пол'
            }),
            "phone": DateInput(attrs={
                'class': 'form-control',
                'id': 'phone',
                'placeholder': 'Номер вашего телефона'
            }),
            "address": DateInput(attrs={
                'class': 'form-control',
                'id': 'address',
                'placeholder': 'Ваш адрес'
            }),
            "number": DateInput(attrs={
                'class': 'form-control',
                'id': 'number',
                'placeholder': 'Ваш номер телефона'
            }),
            "city": DateInput(attrs={
                'class': 'form-control',
                'id': 'city',
                'placeholder': 'Город'
            })
        }


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')