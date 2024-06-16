from django.shortcuts import redirect
from django.template.defaulttags import csrf_token
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, DetailView, UpdateView

from .models import Event
from .forms import EventForm


class AddEvent(CreateView):
    model = Event
    form_class = EventForm
    event = None

    def form_valid(self, form):
        self.event = form.save(commit=False)
        self.event.host = self.request.user
        self.event.save()
        return redirect('event_detail', name=self.event.name)


class EventDetail(DetailView):
    model = Event
    slug_field = "name"
    slug_url_kwarg = "name"


class UpdateEvent(UpdateView):
    model = Event
    slug_field = "name"
    slug_url_kwarg = "name"
