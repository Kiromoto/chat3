from django.urls import path
from .views import MemberView, ChatroomView, MessageView, show_profile
from .views import UserInfoEdit
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

# router.urls

urlpatterns = [path('info/', show_profile, name='show_profile'),
               path('<int:pk>/profile/', UserInfoEdit.as_view(), name='userinfoedit'),
               ] + router.urls



# urlpatterns = [
#                   path('members/', MemberView.as_view({'get': 'show_list'})),
#                   path('members/<int:pk>', MemberView.as_view({'get': 'show_one'})),
#                   path('chatrooms/', ChatroomView.as_view()),
#                   path('chatrooms/<int:pk>', ChatroomView.as_view()),
#                   path('messages/', MessageView.as_view()),
#                   path('messages/<int:pk>', MessageView.as_view()),
#               ] + statics(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
