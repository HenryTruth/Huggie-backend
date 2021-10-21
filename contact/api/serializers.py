from rest_framework.serializers import ModelSerializer,SerializerMethodField, IntegerField
from contact.models import MyRequests
from profiles.api.serializers import ProfileSerializer, UserPublicSerializer


class MyRequestsSerializer(ModelSerializer):
    sender = SerializerMethodField("get_sender_data")
    sender_id = IntegerField(write_only=True)
    receiver = SerializerMethodField("get_receiver_data")
    receiver_id = IntegerField(write_only=True)

    class Meta:
        model = MyRequests
        fields = '__all__'


    def get_receiver_data(self, obj):
        return ProfileSerializer(obj.receiver).data


    def get_sender_data(self, obj):
        return ProfileSerializer(obj.sender).data


