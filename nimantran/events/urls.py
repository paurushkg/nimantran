from django.urls import path

from .views import AddEvent, EventDetail, UpdateEvent, ListEvent, SearchListEvent, AddGuest, UpdateGuest, ListGuest, \
    GuestDetail, SearchListGuest, DeleteGuest, Card

urlpatterns = [
    path('all_events', ListEvent.as_view(), name="list_event"),
    path('search_event', SearchListEvent.as_view(), name="search_event"),
    path('add_event', AddEvent.as_view(), name="add_event"),
    path('view/<str:name>', EventDetail.as_view(), name="event_detail"),
    path('update/<int:pk>', UpdateEvent.as_view(), name="update_event"),


    path('add_guest', AddGuest.as_view(), name="add_guest"),
    path('update_guest/<int:pk>', UpdateGuest.as_view(), name="update_guest"),
    path('list_guest', ListGuest.as_view(), name="list_guest"),
    path('guest_detail/<int:pk>', GuestDetail.as_view(), name="guest_detail"),
    path('search_guest', SearchListGuest.as_view(), name="search_guest"),
    path('guest_delete/<int:pk>', DeleteGuest.as_view(), name="guest_delete"),

    path('card/<str:slug>', Card.as_view(), name="card"),



]
