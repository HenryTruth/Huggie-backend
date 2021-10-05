from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from account.api.permissions import IsOwnerOrReadOnly
from contact.models import Contact
from contact.api.serializers import ContactSerializer


class ContactAPIView(mixins.CreateModelMixin,
generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # # authentication_classes = [SessionAuthentication]
    serializer_class = ContactSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Contact.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self):
        return serializers.save(self.request.user)



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
