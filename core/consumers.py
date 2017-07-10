# coding: utf-8
import json
import logging
import time

from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http

from django_gravatar.helpers import get_gravatar_url

from core.models import Room


log = logging.getLogger(__name__)


@channel_session
@channel_session_user_from_http
def ws_connect(message):
    message.reply_channel.send({"accept": True})
    try:
        prefix, label = message['path'].strip('/').split('/')
        if prefix != 'chat':
            log.debug('invalid ws path=%s', message['path'])
            message.reply_channel.send({"close": True})
            return
        room = Room.objects.get(label=label)
    except ValueError:
        log.debug('invalid ws path=%s', message['path'])
        message.reply_channel.send({"close": True})
        return
    except Room.DoesNotExist:
        log.debug('Room label=%s does not exist.', label)
        message.reply_channel.send({"close": True})
        return

    log.debug('Connecting room=%s client=%s:%s',
              room.label, message['client'][0], message['client'][1])

    Group('chat-%s' % label, channel_layer=message.channel_layer).add(message.reply_channel)

    message.channel_session['room'] = room.label


@channel_session
@channel_session_user
def ws_receive(message):
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
    except KeyError:
        log.debug('No room in channel_session')
        return
    except Room.DoesNotExist:
        log.debug('Room label=%s does not exist.', label)
        return

    try:
        data = json.loads(message['text'])
    except ValueError:
        log.debug("ws message isn't json text=%s", message['text'])
        return

    if data:
        log.debug('Chatting in room=%s: message=%s', room.label, data)
        msg = room.messages.create(**data, sender=message.user)
        if message.user:
            username = message.user.username
            name = message.user.first_name
        else:
            username = None
            name = '[Anonymous]'
        data.update(username=username,
                    name=name,
                    timestamp=time.mktime(msg.timestamp.timetuple()),
                    avatar=message.user and get_gravatar_url(message.user.email) or None)
        Group('chat-%s' % label, channel_layer=message.channel_layer).send({'text': json.dumps(data)})


@channel_session
@channel_session_user
def ws_disconnect(message):
    try:
        label = message.channel_session['room']
        Group('chat-' + label, channel_layer=message.channel_layer).discard(message.reply_channel)
    except (KeyError, Room.DoesNotExist):
        pass
