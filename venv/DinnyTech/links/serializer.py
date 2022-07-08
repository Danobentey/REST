from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers

from links.models import Link

class LinkSerializer(serializers.Serializer):
    class Meta:
        model = Link
        fields = "__all__"