from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from account.api.permissions import IsOwnerOrReadOnly
from contact.models import MyRequests
from contact.api.serializers import MyRequestsSerializer
from Huggies.custom_methods import IsAuthenticatedCustom
from django.conf import settings
import requests



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



class MyRequestsView(ModelViewSet):
    queryset = MyRequests.objects.select_related(
        "sender", "receiver")
    serializer_class = MyRequestsSerializer
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


# class ContactAPIView(mixins.CreateModelMixin,
# generics.ListAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     # # authentication_classes = [SessionAuthentication]
#     serializer_class = MyRequestsSerializer
#     passed_id = None

#     def get_queryset(self):
#         request = self.request
#         qs = MyRequests.objects.all()
#         query = request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def perform_create(self):
#         return serializers.save(self.request.user)



# class ContactAPIDetailView(mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     # authentication_classes = []
#     serializer_class = ContactDetailSeriailizer
#     queryset = Contact.objects.all()
#     lookup_field = 'id'
#     # parser_classes = [MultiPartParser, JSONParser]

#     def put(self,request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
