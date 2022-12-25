from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.generics import UpdateAPIView
from django.views.generic import UpdateView

from rest_framework import viewsets


from .models import Member, Chatroom, Message
from .forms import UserEdit
from django.contrib.auth.models import User
from .serializers import MemberSerializer, ChatroomSerializer, MessageSerializer


class MemberView(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class ChatroomView(viewsets.ModelViewSet):
    serializer_class = ChatroomSerializer
    queryset = Chatroom.objects.all()


class MessageView(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


def show_profile(request):
    return render(request, 'first.html')


class UserInfoEdit(UpdateView):
    # permission_required = ('chatback.change_ad')
    form_class = UserEdit
    model = Member
    template_name = 'userinfo.html'
    context_object_name = 'edit_user_info'
    success_url = reverse_lazy('show_profile')
