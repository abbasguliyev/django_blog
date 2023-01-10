from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from contact.models import Contact
from contact.api.serializers import ContactSerializer
from contact.api.selectors import contact_list
from contact.api.services import create_contact, update_contact

class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = contact_list()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny,]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_contact(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ContactDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = contact_list()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny,]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        update_contact(instance=instance, **serializer.validated_data)
        return Response(serializer.data)