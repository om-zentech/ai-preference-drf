from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.permissions import IsAdminOrSuperAdmin, IsSuperAdmin
from analytics.services.analytics_service import AnalyticsService
from analytics.services.export_csv_service import ExportCSVService

class TotalRevenueView(APIView):
    permission_classes = [IsSuperAdmin]
    
    def get(self, request):
        service = AnalyticsService(request.user)
        result = service.get_total_revenue()

        if "error" in result:
            return Response(result, status=500)

        return Response(result)
    
class TopUsersView(APIView):
    permission_classes = [IsAdminOrSuperAdmin]

    def get(self, request):
        service = AnalyticsService(request.user)
        result = service.get_top_user()
        
        if "error" in result:
            return Response(result, status=500)
        
        return Response(result)
    
class MonthlyUsageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = AnalyticsService(request.user)
        result = service.get_monthly_usage()

        if "error" in result:
            return Response(result, status=500)

        return Response(result)
    
class TopModelsView(APIView):
    permission_classes = [IsAdminOrSuperAdmin]

    def get(self, request):
        service = AnalyticsService(request.user)
        result = service.get_top_model()

        if "error" in result:
            return Response(result, status=500)

        return Response(result)
    
class UserModelUsageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = AnalyticsService(request.user)
        result = service.get_user_model_usage()

        if "error" in result:
            return Response(result, status=500)

        return Response(result)

class UsageLogCSVExportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = ExportCSVService(request.user)
        result = service.get_usage_csv()
        
        if "error" in result:
            return Response(result, status=500)

        return Response(result)