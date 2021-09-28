from django.db import models
from django.contrib.auth.models import User

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100,blank=True)
    sex = models.CharField(max_length=10, choices=SEX_TYPES)
    department = models.CharField(max_length=1000)
    level = models.CharField(max_length=4, choices=LEVELS)
    institution = models.CharField(max_length=2000)
    description = models.CharField(max_length=500)
    profile_pic = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    longtitude = models.IntegerField(null=True,blank=True)
    latitude = models.IntegerField(null=True,blank=True)


    def __str__(self):
         return f'{self.user.username} Details'


    @property
    def owner(self):
        return self.user





