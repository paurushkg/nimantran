from django.urls import path

from .views import AddEvent, EventDetail, UpdateView

urlpatterns = [
    path('add_event', AddEvent.as_view()),
    path('<str:name>', EventDetail.as_view(), name="event_detail"),
    # path('<str:name>', UpdateView.as_view(), name="update_event")
]
