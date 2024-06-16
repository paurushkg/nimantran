from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from django.core.exceptions import ValidationError

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }
        widgets = {
            'full_name': forms.TextInput(attrs={"class": "form-control"}),
            'phone_number': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.TextInput(attrs={"class": "form-control"}),
            'password': forms.PasswordInput(attrs={"class": "form-control"}),

        }

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        if password != self.cleaned_data.get('confirm_password'):
            self.add_error('password', 'Passwords don\'t match')


class UserLoginForm(forms.ModelForm):
    user_cache = None
    error_messages = {
        "invalid_login":
            "Please enter a correct phone number and password. Note that both "
            "fields may be case-sensitive.",
        "inactive": "This account is inactive.",
    }

    class Meta:
        model = User
        fields = ['phone_number', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }
        widgets = {
            'phone_number': forms.TextInput(attrs={"class": "form-control"}),
            'password': forms.PasswordInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        phone_number = self.cleaned_data.get("phone_number")
        password = self.cleaned_data.get("password")

        if phone_number is not None and password:
            self.user_cache = authenticate(
                phone_number=phone_number,
                password=password
            )
            if self.user_cache is None:
                self.add_error('password', self.error_messages['invalid_login'])
        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages["invalid_login"],
            code="invalid_login"
        )
