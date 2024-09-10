from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Event
from .forms import EventForm

# Create your views here.
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {
        'events': events
    })

def event_detail(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'events/event_detail.html', {
        'event': event
    })

def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')

    else:
        form = EventForm()

    return render(request, 'events/event_form.html', {
        'form': form
    })

def event_edit(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')

    else:
        form = EventForm(instance=event)

    return render(request, 'events/event_form.html', {
        'form': form
    })

def event_delete(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        event.delete()
        return redirect('event_list')

    return render(request, 'events/event_confirm_delete.html', {
        'event': event
    })
