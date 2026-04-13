from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from accounts import constants

class CustomTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["role"] = user.role
        token["username"] = user.username
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        if self.user.is_deleted:
            raise serializers.ValidationError(constants.ACCOUNT_DEACTIVATED)
        return data