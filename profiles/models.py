from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):

    SEX_TYPES = (
        ('male', 'male'),
        ('female', 'female')
    )

    LEVELS = (
        ('100L','100L'),
        ('200L', '200L'),
        ('300L','300L'),
        ('400L','400L'),
        ('500L','500L'),
        ('600L','600L'),
        ('700L', '700L')
    )
    user = models.OneToOneField(User, related_name="user_profile",on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100,blank=True)
    sex = models.CharField(max_length=10, choices=SEX_TYPES)
    department = models.CharField(max_length=1000)
    level = models.CharField(max_length=4, choices=LEVELS)
    institution = models.CharField(max_length=2000)
    description = models.CharField(max_length=500, blank=True)
    profile_pic = CloudinaryField('image', null=True)
    longtitude = models.IntegerField(null=True,blank=True)
    latitude = models.IntegerField(null=True,blank=True)
    is_online = models.DateTimeField(default=timezone.now)
    attribute_1 = models.CharField(max_length=30,null=True,blank=True)
    attribute_2 = models.CharField(max_length=30,null=True,blank=True)
    attribute_3 = models.CharField(max_length=30,null=True,blank=True)
    attribute_4 = models.CharField(max_length=30,null=True,blank=True)
    attribute_5 = models.CharField(max_length=30,null=True,blank=True)
    picture_1 = CloudinaryField('image',null=True,blank=True)
    picture_2 = CloudinaryField('image',null=True,blank=True)
    picture_3 = CloudinaryField('image',null=True,blank=True)
    picture_4 = CloudinaryField('image',null=True,blank=True)
    picture_5 = CloudinaryField('image',null=True,blank=True)
    picture_6 = CloudinaryField('image',null=True,blank=True)
    



    class Meta:
        ordering = ['-is_online']


    def __str__(self):
         return f'{self.user.username} Details'


    @property
    def owner(self):
        return self.user





