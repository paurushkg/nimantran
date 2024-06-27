import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from .models import Event
from .forms import EventForm


class ListEvent(LoginRequiredMixin, ListView):
    model = Event

    def get_queryset(self):
        return self.model.objects.filter(host=self.request.user)


class SearchListEvent(LoginRequiredMixin, ListView):
    model = Event

    def get_queryset(self):
        event_query = self.request.GET.get("event_name")
        return self.model.objects.filter(host=self.request.user, name__icontains=event_query)


class AddEvent(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Event
    form_class = EventForm
    event = None

    def get_success_url(self):
        return reverse('event_detail', kwargs={'name': self.event.name})

    def form_valid(self, form):
        self.event = form.save(commit=False)
        self.event.host = self.request.user
        if self.event.date < datetime.date.today():
            messages.error(self.request, "Event Date cannot be in past!")
            return render(self.request, "events/event_form.html", {"form": form})
        try:
            self.event.save()
        except IntegrityError:
            messages.error(self.request, f"There is already an event with name \"{self.event.name}\"")
            return render(self.request, "events/event_form.html", {"form": form})
        return super().form_valid(form)


class EventDetail(DetailView):
    model = Event
    slug_field = "name"
    slug_url_kwarg = "name"
    object = None

    def get_queryset(self):
        return self.model.objects.filter(host=self.request.user)


class UpdateEvent(UpdateView):
    UpdateView.model = Event
    UpdateView.form_class = EventForm
    UpdateView.template_name_suffix = "_update_form"
    event = None

    def form_valid(self, form):
        self.event = form.save(commit=False)
        self.event.host = self.request.user
        if self.event.date < datetime.date.today():
            messages.error(self.request, "Event Date cannot be in past!")
            return render(self.request, "events/event_update_form.html", {"form": form, "object": self.event})
        self.event.save()
        return super().form_valid(form)
