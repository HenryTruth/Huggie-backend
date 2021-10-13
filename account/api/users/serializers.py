import datetime
from django.contrib.auth.models import User
from django.utils import timezone

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.reverse import reverse as api_reverse

from profiles.api.serializers import ProfileDetailSeriailizer
from profiles.models import Profile

class UserDetailSerializer(ModelSerializer):
    uri = SerializerMethodField(read_only=True)
    bio = SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = [
            'uri',
            'id',
            'username',
            'bio',
        ]

    def get_bio(self, obj):
        request = self.context.get('request')
        qs = Profile.objects.filter(id=obj.id)
        res = ProfileDetailSeriailizer(qs, context={"request":request}, many=True).data
        return res

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api-user:detail",kwargs={"id":obj.id}, request=request)