from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Member, Chatroom, Message
from .serializers import MemberSerializer, ChatroomSerializer, MessageSerializer


class MemberViewset(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class ChatroomViewset(viewsets.ModelViewSet):
    queryset = Chatroom.objects.all()
    serializer_class = ChatroomSerializer


class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer



# class MemberView(APIView):
#     def get(self, request):
#         membersall = Member.objects.all()
#         return Response({"All members": membersall})
#
#
# class ChatroomView(APIView):
#     def get(self, request):
#         chatroomsall = Chatroom.objects.all()
#         return Response({"All chatrooms": chatroomsall})
#
#
# class MessageView(APIView):
#     def get(self, request):
#         messagesall = Message.objects.all()
#         return Response({"All messages": messagesall})
