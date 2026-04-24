from ..models import User
from rest_framework.exceptions import ValidationError, NotFound
from accounts.constants import (USER_NOT_FOUND, HAS_SUFFICIENT_PRIVILEGE, PROMOT_USER_TO_ADMIN, ADMIN_NOT_FOUND, 
                                CANT_DEMOTE_YOURSELF, DEMOT_ADMIN_TO_USER, ALREADY_USER)

class AdminService:
    def __init__(self, user, user_id):
        self.user = user
        self.user_id = user_id
        
    def promote_user(self):
        try:
            user = User.objects.get(id=self.user_id)
        except User.DoesNotExist:
            raise NotFound(USER_NOT_FOUND)
            
        if user.role == 'superadmin' or user.role == 'admin':
            raise ValidationError(HAS_SUFFICIENT_PRIVILEGE)
        user.role = "admin"
        user.save()
        return {"message": PROMOT_USER_TO_ADMIN}
    
    def demote_user(self):
        try:
            user = User.objects.get(id=self.user_id)
        except User.DoesNotExist:
            raise NotFound(ADMIN_NOT_FOUND)
        
        if self.user.id == user.id and user.role == 'superadmin':
            raise ValidationError(CANT_DEMOTE_YOURSELF)
        elif user.role == 'user':
            raise ValidationError(ALREADY_USER)
        user.role = "user"
        user.save()
        return {"message": DEMOT_ADMIN_TO_USER}