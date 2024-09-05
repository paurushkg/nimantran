from django import forms
from .models import (
    Event,
    ChildEvent,
    Groom,
    Bride, Guest,
)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'venue', 'date']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'venue': forms.TextInput(attrs={"class": "form-control"}),
            'date': forms.TextInput(attrs={"class": "form-control", "type": "date"}),
        }


class ChildEventForm(forms.ModelForm):
    class Meta:
        model: ChildEvent
        fields = ['name', 'venue', 'date']


class GroomForm(forms.ModelForm):
    class Meta:
        model: Groom
        fields = ['name', 'father', 'mother', ]
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'father': forms.TextInput(attrs={"class": "form-control"}),
            'mother': forms.TextInput(attrs={"class": "form-control"}),
        }


class BrideForm(forms.ModelForm):
    class Meta:
        model: Bride
        fields = ['name', 'father', 'mother', ]
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'father': forms.TextInput(attrs={"class": "form-control"}),
            'mother': forms.TextInput(attrs={"class": "form-control"}),
        }


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        with_family = forms.BooleanField()

        fields = ['name', 'with_family']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
        }
