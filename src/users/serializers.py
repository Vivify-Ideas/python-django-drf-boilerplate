from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from src.users.models import User,Analysis
from src.common.serializers import ThumbnailerJSONSerializer

class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ('analysis','analyst_user')
        read_only_fields = ('analysis_id',)

class UserSerializer(serializers.ModelSerializer):
    profile_picture = ThumbnailerJSONSerializer(required=False, allow_null=True, alias_target='src.users')
    # subscribe_analysts = AnalysisSerializer()
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'profile_picture',
            
           
            
        )
        read_only_fields = ('username',)


class CreateUserSerializer(serializers.ModelSerializer):
    profile_picture = ThumbnailerJSONSerializer(required=False, allow_null=True, alias_target='src.users')
    tokens = serializers.SerializerMethodField()
   

    def get_tokens(self, user):
        return user.get_tokens()

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
            'tokens',
            'profile_picture',
                      
            
        )

        read_only_fields = ('tokens',)
        extra_kwargs = {'password': {'write_only': True}}


class SubscribeAnalists(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('subscribe_analysts',)
    
    
        

    

    
        


    
