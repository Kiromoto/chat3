from django.contrib import admin
from .models import Member, Chatroom, Message


class MemberAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user',)
    search_fields = ('user',)


class ChatroomAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('text',)
    list_filter = ('text',)
    search_fields = ('text',)


admin.site.register(Member, MemberAdmin)
admin.site.register(Chatroom, ChatroomAdmin)
admin.site.register(Message, MessageAdmin)
