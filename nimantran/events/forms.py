from django import forms
from . models import (
    Event,
    ChildEvent,
    Groom,
    Bride,
)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'venue', 'date']


class ChildEventForm(forms.ModelForm):
    class Meta:
        model: ChildEvent
        fields = ['name', 'venue', 'date']


class GroomForm(forms.ModelForm):
    class Meta:
        model: Groom
        fields = ['name', 'father', 'mother', ]


class BrideForm(forms.ModelForm):
    class Meta:
        model: Bride
        fields = ['name', 'father', 'mother', ]
