from accounts.models import User
from accounts.constants import ACCOUNT_DELETE_SUCCESS, USER_NOT_FOUND, ACCOUNT_DELETE_FAIL
from rest_framework.exceptions import APIException

class UserService:
    def __init__(self, user=None):
        self.user = user

    def list_users(self):
        try:
            users = User.objects.filter(is_deleted=False)
            return users
        except Exception:
            raise APIException(USER_NOT_FOUND)

    def delete_profile(self):
        try:
            self.user.delete()
            return {"message": ACCOUNT_DELETE_SUCCESS}
        except Exception:
            raise APIException(ACCOUNT_DELETE_FAIL)