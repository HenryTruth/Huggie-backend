from django.db import models
from profiles.models import Profile

# Create your models here.
class Contact(models.Model):
    contact_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sender_id = models.IntegerField(null=True,blank=True)
    contact_response = models.CharField(default="pending", max_length=50)


    def __str__(self):
        return f'{self.contact_user.username} contact'

