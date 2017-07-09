# coding: utf-8
from django.shortcuts import render
from core.models import Room


def room(request, label):
    room_, is_new = Room.objects.get_or_create(label=label)
    messages = room_.messages.order_by('-timestamp')[:20]

    return render(request, 'room.html', {
        'room': room_,
        'messages': messages,
    })


def index(request):
    return render(request, 'index.html')
