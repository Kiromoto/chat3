from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Member, Chatroom, Message


class MemberView(APIView):
    def get(self, request):
        membersall = Member.objects.all()
        return Response({"All members": membersall})


class ChatroomView(APIView):
    def get(self, request):
        chatroomsall = Chatroom.objects.all()
        return Response({"All chatrooms": chatroomsall})


class MessageView(APIView):
    def get(self, request):
        messagesall = Message.objects.all()
        return Response({"All messages": messagesall})
