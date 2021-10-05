from rest_framework.serializers import ModelSerializer,SerializerMethodField
from profiles.models import Profile
from django.contrib.auth.models import User
from django.db.models import Q

from message.models import GenericFileUpload, Message, MessageAttachment

class UserPublicSerializer(ModelSerializer):
    message_count = SerializerMethodField()
    class Meta:
        model = User 
        fields = [
            'id',
            'username',
            'message_count'
            # 'uri'
        ]

        read_only_fields = ['username']

    def get_message_count(self, obj):
        try:
            user_id = self.context["request"].id
        except Exception as e:
            user_id = None

        # from message_control.models import Message
        message = Message.objects.filter(Q(sender_id=obj.id, receiver_id=user_id) | Q(
                sender_id=obj.id, receiver_id=user_id)).distinct()

        return message.count()


class ProfileSerializer(ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    message_count = SerializerMethodField()

    class Meta: 
        model = Profile
        fields = "__all__"

    def get_message_count(self, obj):
        try:
            user_id = self.context["request"].user.id
        except Exception as e:
            user_id = None

        # from message_control.models import Message
        message = Message.objects.filter(Q(sender_id=user_id, receiver_id=user_id) | Q(
                sender_id=user_id, receiver_id=user_id)).distinct()

        return message.count()


class ProfileDetailSeriailizer(ModelSerializer):
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"

    def get_message_count(self, obj):
        try:
            user_id = self.context["request"].user.id
        except Exception as e:
            user_id = None

        # from message_control.models import Message
        message = Message.objects.filter(sender_id=obj.user.id, receiver_id=user_id, is_read=False).distinct()

        return message.count()


    read_only_fields = ['user']




        
