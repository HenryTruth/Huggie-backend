from rest_framework import serializers
from profiles.models import Profile
from message.models import GenericFileUpload, Message, MessageAttachment
from profiles.api.serializers import ProfileSerializer, UserPublicSerializer

class GenericFileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenericFileUpload
        fields = "__all__"



class MessageAttachmentSerializer(serializers.ModelSerializer):
    attachment = GenericFileUploadSerializer()

    class Meta:
        model = MessageAttachment
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField("get_sender_data")
    sender_id = serializers.IntegerField(write_only=True)
    receiver = serializers.SerializerMethodField("get_receiver_data")
    receiver_id = serializers.IntegerField(write_only=True)
    message_attachments = MessageAttachmentSerializer(
        read_only=True, many=True)

    class Meta:
        model = Message
        fields = "__all__"

    def get_receiver_data(self, obj):
        return UserPublicSerializer(obj.receiver.user).data

    def get_sender_data(self, obj):
        return UserPublicSerializer(obj.sender.user).data
