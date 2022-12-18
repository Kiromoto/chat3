from django.urls import path
from .views import MemberView, ChatroomView, MessageView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

app_name_member = "members"
app_name_chatroom = "chatrooms"
app_name_message = "messages"

urlpatterns = [
                  path('members/', MemberView.as_view()),
                  path('members/<int:pk>', MemberView.as_view()),
                  path('chatrooms/', ChatroomView.as_view()),
                  path('chatrooms/<int:pk>', ChatroomView.as_view()),
                  path('messages/', MessageView.as_view()),
                  path('messages/<int:pk>', MessageView.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
