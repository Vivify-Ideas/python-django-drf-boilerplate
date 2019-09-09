from rest_framework import serializers
from .models import MyFile


class MyFileSerializer(serializers.ModelSerializer):
    class Meta():
        model = MyFile
        fields = ('file', 'description', 'uploaded_at')