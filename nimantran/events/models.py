from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Event(models.Model):
    name = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    date = models.DateField()
    host = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'host'], name='unique_event_host_combination'
            )
        ]

    def __str__(self):
        return self.name + "_" + self.host.full_name

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'name': self.name})


class ChildEvent(models.Model):
    name = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    date = models.DateField()
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "_" + self.event.name + self.event.host.full_name


class Bride(models.Model):
    name = models.CharField(max_length=255)
    father = models.CharField(max_length=255)
    mother = models.CharField(max_length=255)
    event = models.OneToOneField(to=Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "_" + self.event.name + self.event.host.full_name


class Groom(models.Model):
    name = models.CharField(max_length=255)
    father = models.CharField(max_length=255)
    mother = models.CharField(max_length=255)
    event = models.OneToOneField(to=Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
