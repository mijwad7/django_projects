from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=50)
    organizer = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.title