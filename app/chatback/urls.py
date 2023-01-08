from django.urls import path
from .views import MemberView, ChatroomView, MessageView, AllMembersList
from .views import show_profile, update_profile
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'members', MemberView, basename='memberurl')
router.register(r'chatrooms', ChatroomView, basename='chatroomurl')
router.register(r'messages', MessageView, basename='messageurl')

app_name_member = "members"
app_name_chatroom = "chatrooms"
app_name_message = "messages"

urlpatterns = [path('profile/', show_profile, name='show_profile'),
               path('editmyprofile/<int:pk>', update_profile, name='update_profile'),
               path('allmembers/', AllMembersList.as_view(), name='allmemberslist')
               ] + router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
