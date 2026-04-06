from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company, AIProduct, AIModel
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import CompanySerializer, AIProductSerializer, AIModelSerializer

class CompanyListCreateView(APIView):
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsAdminUser()]

    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class AIProductListCreateView(APIView):
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsAdminUser()]

    def get(self, request):
        products = AIProduct.objects.all()
        serializer = AIProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AIProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AIModelListCreateView(APIView):
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsAdminUser()]

    def get(self, request):
        models = AIModel.objects.all()
        serializer = AIModelSerializer(models, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AIModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)