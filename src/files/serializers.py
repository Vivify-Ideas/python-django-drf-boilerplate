from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'thumbnail', 'created_at', 'id')

    #--this code ensures that instances created through the serializer are correctly associated with their creators
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author_id'] = user.id

        return super().create(validated_data)
