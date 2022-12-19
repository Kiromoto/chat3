from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Member, Chatroom, Message
from django.contrib.auth.models import User
from .serializers import MemberSerializer, ChatroomSerializer, MessageSerializer


class MemberView(APIView):
    def get(self, request):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response({"All members": serializer.data})

    def post(self, request):
        members = request.data.get('members')
        serializer = MemberSerializer(data=members)
        if serializer.is_valid(raise_exception=True):
            member_saved = serializer.save()
        return Response({"success": f'Member {member_saved.online} created successfully'})

    def put(self, request, pk):
        saved_member = get_object_or_404(Member.objects.all(), pk=pk)
        data = request.data.get('members')
        serializer = MemberSerializer(instance=saved_member, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            member_saved = serializer.save()
            # print(f'{User.objects.get(id=member_saved.user_id)}')
        return Response({
            "success": f"Member '{member_saved.user_id}' updated successfully"
        })

    def delete(self, request, pk):
        member = get_object_or_404(Member.objects.all(), pk=pk)
        member_name = member.user.username
        member.delete()
        return Response({
            "message": f"Member {member_name} has been deleted."
        }, status=204)


class ChatroomView(APIView):
    def get(self, request):
        chatrooms = Chatroom.objects.all()
        serializer = ChatroomSerializer(chatrooms, many=True)
        return Response({"All chatrooms": serializer.data})

    def post(self, request):
        chatrooms = request.data.get('chatrooms')
        serializer = ChatroomSerializer(data=chatrooms)
        if serializer.is_valid(raise_exception=True):
            chatroom_saved = serializer.save()
        return Response({"success": f'Chatroom {chatroom_saved.name} created successfully'})

    def put(self, request, pk):
        saved_chatroom = get_object_or_404(Chatroom.objects.all(), pk=pk)
        data = request.data.get('chatrooms')
        serializer = ChatroomSerializer(instance=saved_chatroom, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            chatroom_saved = serializer.save()
        return Response({
            "success": f"Chatroom '{chatroom_saved.name}' updated successfully"
        })

    def delete(self, request, pk):
        chatroom = get_object_or_404(Chatroom.objects.all(), pk=pk)
        chatroom_name = chatroom.name
        chatroom.delete()
        return Response({
            "message": f"Chatroom {chatroom_name} has been deleted."
        }, status=204)



class MessageView(APIView):
    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response({"All messages": serializer.data})

    def post(self, request):
        messages = request.data.get('messages')
        serializer = MessageSerializer(data=messages)
        if serializer.is_valid(raise_exception=True):
            message_saved = serializer.save()
        return Response({"success": f'Message {message_saved.text} created successfully'})

    def put(self, request, pk):
        saved_message = get_object_or_404(Message.objects.all(), pk=pk)
        data = request.data.get('messages')
        serializer = MessageSerializer(instance=saved_message, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            message_saved = serializer.save()
        return Response({
            "success": f"Message '{message_saved.text}' updated successfully"
        })

    def delete(self, request, pk):
        message = get_object_or_404(Message.objects.all(), pk=pk)
        message.delete()
        return Response({
            "message": f"Message with id: {pk} has been deleted."
        }, status=204)
