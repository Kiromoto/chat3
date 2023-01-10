from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from rest_framework.generics import UpdateAPIView
from django.views.generic import UpdateView, ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction

from rest_framework import viewsets

from .models import Member, Chatroom, Message
from .forms import UserForm, ProfileForm
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

class AllMembersList(ListView):
    model = User
    ordering = 'username'
    template_name = 'allmemberslist.html'
    context_object_name = 'allmemberslist'
    paginate_by = 20

    def get_context_date(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['numbers'] = 20
        print(context)
        return context


def show_profile(request, *args, **kwargs):
    return render(request, 'userinfo.html')


@login_required
@transaction.atomic
def update_profile(request, pk):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.member)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль был успешно обновлен!')
            return redirect('show_profile')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.member)
    return render(request, 'edituserinfo.html', {'user_form': user_form, 'profile_form': profile_form})
