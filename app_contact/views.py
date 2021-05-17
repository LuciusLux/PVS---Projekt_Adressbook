from django.shortcuts import render

from rest_framework import viewsets
from .models import Contact, Address
from .serializers import ContactSerializer, AddressSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.

class ContactApiView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['type']
    search_fields = ['name', 'first_name']




class AddressApiView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()