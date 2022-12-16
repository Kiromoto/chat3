from .models import Member, Chatroom, Message
from rest_framework import serializers


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['user', 'avatar', 'online',]


class ChatroomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chatroom
        fields = ['name', 'dtcreate', 'owner', 'guests',]


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['text', 'dtcreate', 'author', 'room',]
