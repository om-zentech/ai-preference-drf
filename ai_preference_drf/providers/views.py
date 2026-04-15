from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company, AIProduct, AIModel
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminOrSuperAdmin
from .serializers import CompanySerializer, AIProductSerializer, AIModelSerializer
from providers import constants

class CompanyListCreateView(APIView):
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminOrSuperAdmin()]
        return [IsAuthenticated()]

    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response({'message':constants.COMPANY_RETRIEVED_SUCCESS, 'data':serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':constants.COMPANY_CREATED_SUCCESS, 'data':serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.data)
    
class CompanyDetailView(APIView):

    def get_permissions(self):
        if self.request.method == 'PUT':
            return [IsAdminOrSuperAdmin()]
        return [IsAuthenticated()]

    def get_object(self, pk):
        return get_object_or_404(Company, pk=pk)

    def get(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class AIProductListCreateView(APIView):
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminOrSuperAdmin()]
        return [IsAuthenticated()]

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
    
class AIProductDetailView(APIView):

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminOrSuperAdmin()]
        return [IsAuthenticated()]

    def get_object(self, pk):
        return get_object_or_404(AIProduct, pk=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = AIProductSerializer(product)
        return Response(serializer.data)

    def patch(self, request, pk):
        product = self.get_object(pk)
        serializer = AIProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AIModelListCreateView(APIView):
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminOrSuperAdmin()]
        return [IsAuthenticated()]

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
    
class AIModelDetailView(APIView):

    def get_permissions(self):
        if self.request.method == "PUT":
            return [IsAdminOrSuperAdmin()]
        return [IsAuthenticated()]

    def get_object(self, pk):
        return get_object_or_404(AIModel, pk=pk)

    def get(self, request, pk):
        model = self.get_object(pk)
        serializer = AIModelSerializer(model)
        return Response(serializer.data)

    def patch(self, request, pk):
        model = self.get_object(pk)
        serializer = AIModelSerializer(model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)