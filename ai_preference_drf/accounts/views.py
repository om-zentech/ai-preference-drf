from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, ProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .tokens import CustomTokenSerializer
from .permissions import IsSuperAdmin
from accounts.services import admin_service, auth_service, user_service

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        service = auth_service.AuthService(request.data)
        data = service.register_user()
        return Response(data, status=status.HTTP_201_CREATED)
    
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
        service = user_service.UserService()
        users = service.list_users()
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data)
    
class DeleteProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        service = user_service.UserService(request.user)
        data = service.delete_profile()
        return Response(data)
    
class PromoteUserView(APIView):
    permission_classes = [IsSuperAdmin]

    def post(self, request, user_id):
        service = admin_service.AdminService(request.user, user_id)
        data = service.promote_user()
        return Response(data, status=status.HTTP_200_OK)
        
class DemoteUserView(APIView):
    permission_classes = [IsSuperAdmin]

    def post(self, request, user_id):
        service = admin_service.AdminService(request.user, user_id)
        data = service.demote_user()
        return Response(data, status=status.HTTP_200_OK)