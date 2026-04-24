from rest_framework.exceptions import ValidationError
from accounts.serializers import RegisterSerializer
from accounts.constants import USER_REGISTER_SUCCESSFUL

class AuthService:
    def __init__(self, data):
        self.data = data

    def register_user(self):
        serializer = RegisterSerializer(data=self.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        serializer.save()
        return {"message": USER_REGISTER_SUCCESSFUL, "data": serializer.data}