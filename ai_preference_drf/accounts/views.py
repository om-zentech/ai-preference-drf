from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, ProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .tokens import CustomTokenSerializer
from .permissions import IsSuperAdmin
from .models import User
from accounts.constants import (USER_REGISTER_SUCCESSFUL, PROMOT_USER_TO_ADMIN, USER_NOT_FOUND,
                                DEMOT_ADMIN_TO_USER, ADMIN_NOT_FOUND, CANT_DEMOTE_YOURSELF, ALREADY_SUPERADMIN, ACCOUNT_DELETE_SUCCESS)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": USER_REGISTER_SUCCESSFUL, "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
    
class UserListView(APIView):
    permission_classes = [IsSuperAdmin]

    def get(self, request):
        users = User.objects.filter(is_deleted=False)
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data)
    
class DeleteProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"message": ACCOUNT_DELETE_SUCCESS})
    
class PromoteUserView(APIView):
    permission_classes = [IsSuperAdmin]

    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            
            if request.user.id == user.id and user.role == 'superadmin':
                return Response({"error": ALREADY_SUPERADMIN}, status=status.HTTP_400_BAD_REQUEST)
            user.role = "admin"
            user.save()
            return Response({"message": PROMOT_USER_TO_ADMIN}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": USER_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        
class DemoteUserView(APIView):
    permission_classes = [IsSuperAdmin]

    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            
            if request.user.id == user.id and user.role == 'superadmin':
                return Response({"error": CANT_DEMOTE_YOURSELF}, status=status.HTTP_400_BAD_REQUEST)
                
            user.role = "user"
            user.save()
            return Response({"message": DEMOT_ADMIN_TO_USER}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": ADMIN_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)