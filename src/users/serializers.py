from rest_framework import serializers

from src.users.models import User
from src.common.serializers import ThumbnailerJSONSerializer

class UserSerializer(serializers.ModelSerializer):
    profile_picture = ThumbnailerJSONSerializer(required=False,
                                                allow_null=True,
                                                alias_target='src.users')

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'profile_picture',
            'is_active',
        )
        read_only_fields = ('username', 'is_active', )


class CreateUserSerializer(serializers.ModelSerializer):
    profile_picture = ThumbnailerJSONSerializer(required=False, allow_null=True, alias_target='src.users')

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'profile_picture',
            'is_active',
        )
        read_only_fields = ('is_active', )
        extra_kwargs = {'password': {'write_only': True}}
