from django.urls import path
# from .views import MemberView, ChatroomView, MessageView
from .views import MemberViewset, ChatroomViewset, MessageViewset
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

app_name_member = "members"
app_name_chatroom = "chatrooms"
app_name_message = "messages"

urlpatterns = [
                  path('members/', MemberViewset.as_view()),
                  path('chatrooms/', ChatroomViewset.as_view()),
                  path('messages/', MessageViewset.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
