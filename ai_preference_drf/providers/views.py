from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminOrSuperAdmin
from providers.services.company_service import CompanyService
from providers.services.product_service import AIProductService
from providers.services.model_service import AIModelService

class CompanyListCreateView(APIView):

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminOrSuperAdmin()]
        return [IsAuthenticated()]

    def get(self, request):
        service = CompanyService()
        result = service.list_companies()

        if "error" in result:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        service = CompanyService()
        result = service.create_company(request.data)

        if "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_201_CREATED)
    
class CompanyDetailView(APIView):

    def get_permissions(self):
        if self.request.method == 'PATCH':
            return [IsAdminOrSuperAdmin()]
        return [IsAuthenticated()]

    def get(self, request, pk):
        service = CompanyService()
        result = service.get_company(pk)

        if "error" in result:
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        return Response(result, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        service = CompanyService()
        result = service.update_company(pk, request.data)

        if "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)
    
class AIProductListCreateView(APIView):
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminOrSuperAdmin()]
        return [IsAuthenticated()]

    def get(self, request):
        service = AIProductService()
        result = service.list_products()

        if "error" in result:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        service = AIProductService()
        result = service.create_product(request.data)

        if "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_201_CREATED)
    
class AIProductDetailView(APIView):

    def get_permissions(self):
        if self.request.method == 'PATCH':
            return [IsAdminOrSuperAdmin()]
        return [IsAuthenticated()]

    def get(self, request, pk):
        service = AIProductService()
        result = service.get_product(pk)

        if "error" in result:
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        return Response(result, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        service = AIProductService()
        result = service.update_product(pk, request.data)

        if "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)

class AIModelListCreateView(APIView):
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminOrSuperAdmin()]
        return [IsAuthenticated()]

    def get(self, request):
        service = AIModelService()
        result = service.list_models()

        if "error" in result:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        service = AIModelService()
        result = service.create_model(request.data)

        if "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_201_CREATED)    

class AIModelDetailView(APIView):

    def get_permissions(self):
        if self.request.method == "PATCH":
            return [IsAdminOrSuperAdmin()]
        return [IsAuthenticated()]

    def get(self, request, pk):
        service = AIModelService()
        result = service.get_model(pk)

        if "error" in result:
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        return Response(result, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        service = AIModelService()
        result = service.update_model(pk, request.data)

        if "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)