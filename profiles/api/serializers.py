from rest_framework.serializers import ModelSerializer,SerializerMethodField
from profiles.models import Profile
from django.contrib.auth.models import User


class UserPublicSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = [
            'id',
            'username',
            # 'uri'
        ]

        read_only_fields = ['username']


class ProfileSerializer(ModelSerializer):
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'firstname',
            'lastname',
            'sex',
            'department',
            'level',
            'institution',
            'description',
            'profile_pic',
            'longtitude',
            'latitude'
        ]


class ProfileDetailSeriailizer(ModelSerializer):
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'firstname',
            'lastname',
            'sex',
            'department',
            'level',
            'institution',
            'description',
            'profile_pic',
            'longtitude',
            'latitude'
        ]

    read_only_fields = ['user','sex']




        
