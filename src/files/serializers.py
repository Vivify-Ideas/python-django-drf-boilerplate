from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = ('file', 'thumbnail', 'created_at', 'id')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author_id'] = user.id

        return super().create(validated_data)
