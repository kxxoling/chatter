# coding: utf-8
import time
from django.http import JsonResponse
from django_gravatar.helpers import get_gravatar_url

from core.models import Room


def to_json(message):
    data = {
        'id': message.id,
        'message': message.message,
        'timestamp': time.mktime(message.timestamp.timetuple()),
    }
    if message.sender:
        data.update({
            'name': message.sender.first_name,
            'username': message.sender.username,
            'avatar': get_gravatar_url(message.sender.email),
            'id': message.sender.id,
        })
    else:
        data.update({
            'name': None,
            'username': None,
            'avatar': get_gravatar_url(''),
            'id': None,
        })
    return data


def room(request, label):
    room_, is_new = Room.objects.get_or_create(label=label)
    messages = room_.messages.order_by('-timestamp')[:20]

    return JsonResponse({
        'room': {
            'id': room_.id,
            'name': room_.name,
            'label': room_.label,
        },
        'messages': [to_json(message) for message in messages[::-1]],
    })
