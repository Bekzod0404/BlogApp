from django import forms

from Bekzod.models import UserRegisterModel, UserLoginModel


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserRegisterModel
        fields = "__all__"
        widgets = {
            "password": forms.PasswordInput
        }


class UserLoginForm(forms.Form):
    class Meta:
        model = UserLoginModel
        fields = "__all__"
        widgets = {
            "password": forms.PasswordInput
        }
