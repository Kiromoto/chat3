from .models import Member, Chatroom, Message
from rest_framework import serializers


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['user', 'online', ]


class ChatroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatroom
        fields = ['name', 'dtcreate', 'owner', 'guests', ]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text', 'dtcreate', 'author', 'room', ]

#
# class MemberSerializer(serializers.Serializer):
#     user_id = serializers.IntegerField()
#     avatar = serializers.ImageField()
#     online = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Member.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.user_id = validated_data.get('user_id', instance.user_id)
#         instance.avatar = validated_data.get('avatar', instance.avatar)
#         instance.online = validated_data.get('online', instance.online)
#
#         instance.save()
#         return instance


# class ChatroomSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     dtcreate = serializers.DateTimeField()
#     owner_id = serializers.IntegerField()
#     # guest = serializers.
#
#     def create(self, validated_data):
#         return Chatroom.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.dtcreate = validated_data.get('dtcreate', instance.dtcreate)
#         instance.owner_id = validated_data.get('owner_id', instance.owner_id)
#         instance.save()
#         return instance

# class MessageSerializer(serializers.Serializer):
#     text = serializers.CharField()
#     dtcreate = serializers.DateTimeField()
#     author_id = serializers.IntegerField()
#     room_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Message.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.text = validated_data.get('text', instance.text)
#         instance.dtcreate = validated_data.get('dtcreate', instance.dtcreate)
#         instance.author_id = validated_data.get('author_id', instance.author_id)
#         instance.room_id = validated_data.get('room_id', instance.room_id)
#         instance.save()
#         return instance
