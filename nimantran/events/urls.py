from django.urls import path

from .views import AddEvent, EventDetail, UpdateEvent, ListEvent, SearchListEvent

urlpatterns = [
    path('all_events', ListEvent.as_view(), name="list_event"),
    path('search_event', SearchListEvent.as_view(), name="search_event"),
    path('add_event', AddEvent.as_view(), name="add_event"),
    path('view/<str:name>', EventDetail.as_view(), name="event_detail"),
    path('update/<int:pk>', UpdateEvent.as_view(), name="update_event")
]
