import datetime
from random import randint

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

from .models import Event, Guest
from .forms import EventForm, GuestForm

ALPHANUMERIC = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    '-'
]


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


class AddGuest(CreateView):
    CreateView.model = Guest
    CreateView.form_class = GuestForm
    guest = None

    def get_success_url(self):
        return reverse('guest_detail', kwargs={'pk': self.guest.pk})

    def form_valid(self, form):
        slug = ''
        for i in range(11):
            index = randint(0, len(ALPHANUMERIC) - 1)
            slug += ALPHANUMERIC[index]

        self.guest = form.save(commit=False)
        if form.is_valid():
            self.guest.slug = slug
        self.guest.save()
        return super().form_valid(form)


class UpdateGuest(UpdateView):
    UpdateView.model = Guest
    UpdateView.form_class = GuestForm
    guest = None

    def get_success_url(self):
        return reverse('guest_detail', kwargs={'pk': self.guest.pk})

    def form_valid(self, form):
        if form.is_valid():
            self.guest = form.save(commit=False)
            self.guest.save()
        return super().form_valid(form)


class ListGuest(ListView):
    ListView.model = Guest
    ListView.form_class = GuestForm


class GuestDetail(DetailView):
    DetailView.model = Guest
    slug_field = "name"
    slug_url_kwarg = "name"
    object = None


class SearchListGuest(LoginRequiredMixin, ListView):
    model = Guest

    def get_queryset(self):
        event_query = self.request.GET.get("guest_name")
        return self.model.objects.filter(name__icontains=event_query)


class DeleteGuest(DeleteView):
    model = Guest

    def get_success_url(self):
        return reverse('list_guest')


class Card(DetailView):
    DetailView.model = Guest
    slug_field = "slug"
    slug_url_kwarg = "slug"
    DetailView.template_name = "card.html"
