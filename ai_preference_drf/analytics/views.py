from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum, Value, F
from django.db.models.functions import Coalesce
from usage.models import UsageLog
from decimal import Decimal
from .serializers import TotalRevenueSerializer, TopUserSerializer, TopModelSerializer, MonthlyUsageSerializer, UserModelUsageSerializer
from accounts.permissions import IsAdminOrSuperAdmin, IsSuperAdmin
from analytics.services.analytics_service import AnalyticsService
from analytics import constants
from io import StringIO
import csv
from django.core.mail import EmailMessage

class TotalRevenueView(APIView):
    permission_classes = [IsSuperAdmin]
    
    def get(self, request):
        try:
            data = (UsageLog.objects.values(model_name=F('model__model_name')).annotate(total_revenue=Coalesce(Sum('cost'),Decimal('0.0'))))
            serializer = TotalRevenueSerializer(data, many=True)
            return Response(serializer.data)
        except Exception:
            return Response({'error':constants.FAILED_TO_FETCH}, status=500)
    
class TopUsersView(APIView):
    permission_classes = [IsAdminOrSuperAdmin]

    def get(self, request):
        data = (UsageLog.objects.values('user__username').annotate(
            total_cost=Coalesce(Sum('cost'), Value(Decimal('0.0'))),
            total_tokens=Coalesce(Sum('tokens_used'), Value(0)),
            total_requests=Coalesce(Sum('request_count'), Value(0))).order_by('-total_cost'))
        serializer = TopUserSerializer(data, many=True)
        return Response(serializer.data)
    
class MonthlyUsageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = AnalyticsService(request.user)
        data = service.get_monthly_usage()
        serializer = MonthlyUsageSerializer(data, many=True)
        return Response(serializer.data)
    
class TopModelsView(APIView):
    permission_classes = [IsAdminOrSuperAdmin]

    def get(self, request):
        data = (UsageLog.objects.values(model_name=F('model__model_name')).annotate(total_tokens=Sum('tokens_used')).order_by('-total_tokens')[:5])
        serializer = TopModelSerializer(data, many=True)
        return Response(serializer.data)
    
class UserModelUsageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = AnalyticsService(request.user)
        data = service.get_user_model_usage()
        serializer = UserModelUsageSerializer(data, many=True)
        return Response(serializer.data)

class UsageLogCSVExportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            buffer = StringIO()
            writer = csv.writer(buffer)
            writer.writerow([
                'Model', 'Product',
                'Tokens Used', 'Request Count',
                'Cost', 'Created At'])
            usage_logs = UsageLog.objects.filter(user=request.user).select_related('user', 'model__product')
            for log in usage_logs:
                writer.writerow([
                    log.model.model_name,
                    log.model.product.product_name,
                    log.tokens_used,
                    log.request_count,
                    log.cost,
                    log.created_at
                ])
            buffer.seek(0)
            
            email = EmailMessage(subject=constants.EMAIL_SUBJECT, body=constants.EMAIL_BODY, to=[request.user.email],)
            email.attach(filename=constants.CSV_FILE_NAME, content=buffer.getvalue(), mimetype="text/csv")
            email.send(fail_silently=False)            
            return Response({"message": constants.EMAIL_SENT_SUCCESS})

        except Exception as e:
            return Response({"error": constants.EMAIL_SENT_FAIL}, status=500)