from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)

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
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        if password != self.cleaned_data.get('confirm_password'):
            self.add_error('password', 'Passwords don\'t match')

