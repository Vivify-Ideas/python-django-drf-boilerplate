from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    profile_picture = VersatileImageFieldSerializer(required=False,
                                                    allow_null=True,
                                                    sizes='profile_picture')

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'profile_picture',
        )
        read_only_fields = ('username', )


class CreateUserSerializer(serializers.ModelSerializer):
    profile_picture = VersatileImageFieldSerializer(required=False,
                                                    allow_null=True,
                                                    sizes='profile_picture')

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
            'auth_token',
            'profile_picture',
        )
        read_only_fields = ('auth_token', )
        extra_kwargs = {'password': {'write_only': True}}
