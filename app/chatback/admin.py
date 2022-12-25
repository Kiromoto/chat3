from django.contrib import admin
from .models import Member, Chatroom, Message


class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'online', 'avatar')
    list_filter = ('user', 'online',)


class ChatroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'dtcreate', 'owner',)
    list_filter = ('name', 'dtcreate', 'owner',)
    search_fields = ('name', 'owner',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'dtcreate', 'author', 'room',)
    list_filter = ('text', 'dtcreate', 'author', 'room',)
    search_fields = ('text', 'author', 'room',)


admin.site.register(Member, MemberAdmin)
admin.site.register(Chatroom, ChatroomAdmin)
admin.site.register(Message, MessageAdmin)
