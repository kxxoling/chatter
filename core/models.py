# coding: utf-8
from django.db.models import Model
from django.db.models.fields import TextField, SlugField, DateTimeField, CharField
from django.db.models import ForeignKey
from django.contrib.auth import get_user_model


User = get_user_model()


class Room(Model):
    name = CharField(max_length=100)
    label = SlugField(unique=True)

    def __str__(self):
        return '<Room - %s>' % self.label


class Message(Model):
    sender = ForeignKey(User, related_name='messages', null=True)
    room = ForeignKey(Room, related_name='messages')
    message = TextField()
    timestamp = DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return '<Message - %s>' % self.message
