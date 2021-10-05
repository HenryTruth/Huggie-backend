from django.contrib import admin
from .models import Message, GenericFileUpload, MessageAttachment

# Register your models here.
admin.site.register(Message)
admin.site.register(GenericFileUpload)
admin.site.register(MessageAttachment)