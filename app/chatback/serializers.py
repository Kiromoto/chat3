from models import Member, Chatroom, Message
from rest_framework import serializers


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['user', ]


class ChatroomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chatroom
        fields = ['name', ]


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['text', ]
