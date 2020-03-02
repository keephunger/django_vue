from django.db import models
from rest_framework import serializers


class Message(models.Model):
    text = models.CharField(max_length=200)
    status = models.BooleanField(default=0)
    edit = models.BooleanField(default=0)
    show = models.BooleanField(default=1)


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'text', 'status', 'pk','edit','show')
