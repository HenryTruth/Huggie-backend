from django.db import models
from profiles.models import Profile

# Create your models here.
class MyRequests(models.Model):
    sender = models.ForeignKey(Profile, related_name="sender_notification", on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey(Profile, related_name="receiver_notification", on_delete=models.CASCADE, null=True)
    my_response = models.CharField(default="#d7880d", max_length=50)


    def __str__(self):
        return f"{self.sender.user.username} send's a date request to {self.receiver.user.username}"

