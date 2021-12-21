from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from rest_framework import permissions
from .serializers import ContactSerializer
# Create your views here.

class ContactsList(ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)


class ContactsDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated)
    lookup_field = "id" # /contacts/1 (search like this)    
    
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
