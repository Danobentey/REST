from os import link
from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView

from links.models import Link
from links.serializer import LinkSerializer

# Create your views here.

class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class CreateApiView(ListCreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi(DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
