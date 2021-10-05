from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from message.api.serializers import GenericFileUpload, GenericFileUploadSerializer, Message, MessageAttachment, MessageSerializer
from rest_framework.response import Response
from Huggies.custom_methods import IsAuthenticatedCustom
from django.db.models import Q
from django.conf import settings
import requests
import json



def handleRequest(serializerData):
    notification = {
        "message": serializerData.data.get("message"),
        "from": serializerData.data.get("sender"),
        "receiver": serializerData.data.get("receiver").get("id"),
        "message_attachments":serializerData.data.get("message_attachments"),
        "is_read":serializerData.data.get("is_read"),
        "created_at":serializerData.data.get("created_at")
    }
    print(settings.SOCKET_SERVER)

    headers = {
        'Content-Type': 'application/json',
    }
    try:
        requests.post(settings.SOCKET_SERVER, json.dumps(
            notification), headers=headers)
    except Exception as e:
        pass 











        
    return True


class GenericFileUploadView(ModelViewSet):
    queryset = GenericFileUpload.objects.all()
    serializer_class = GenericFileUploadSerializer


class MessageView(ModelViewSet):
    queryset = Message.objects.select_related(
        "sender", "receiver").prefetch_related("message_attachments")
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticatedCustom, )

    def get_queryset(self):
        data = self.request.query_params.dict()
        user_id = data.get("user_id", None)

        if user_id:
            active_user_id = self.request.user.id
            return self.queryset.filter(Q(sender_id=user_id, receiver_id=active_user_id) | Q(
                sender_id=active_user_id, receiver_id=user_id)).distinct()
        return self.queryset

    def create(self, request, *args, **kwargs):

        try:
            request.data._mutable = True
        except:
            pass
        attachments = request.data.pop("attachments", None)

        if str(request.user.id) != str(request.data.get("sender_id", None)):
            raise Exception("only sender can create a message")

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if attachments:
            MessageAttachment.objects.bulk_create([MessageAttachment(
                **attachment, message_id=serializer.data["id"]) for attachment in attachments])

            message_data = self.get_queryset().get(id=serializer.data["id"])
            return Response(self.serializer_class(message_data).data, status=201)

        handleRequest(serializer)

        return Response(serializer.data, status=201)




class ReadMultipleMessages(APIView):

    def post(self, request):
        data = request.data.get("message_ids", None)

        Message.objects.filter(id__in=data).update(is_read=True)
        return Response("success")