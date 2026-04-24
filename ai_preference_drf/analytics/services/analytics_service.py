from usage.models import UsageLog
from decimal import Decimal
from django.db.models.functions import Coalesce, TruncMonth
from django.db.models import Sum, F, Value
from analytics.serializers import TotalRevenueSerializer
from analytics.serializers import UserModelUsageSerializer, MonthlyUsageSerializer, TopUserSerializer, TopModelSerializer
from analytics.constants import (MODEL_USAGE_RETRIEVED_SUCCESS, FAILED_TO_FETCH, MONTHLY_USAGE_RETRIEVED_SUCCESS, TOP_MODEL_RETRIEVED_SUCCESS,
                                 REVENUE_RETRIEVED_SUCCESS, TOP_USER_RETRIEVED_SUCCESS)

class AnalyticsService:
    def __init__(self, user):
        self.user = user
        
    def get_user_model_usage(self):
        try:
            data = (
                UsageLog.objects.filter(user=self.user).values(model_name=F('model__model_name')).annotate(
                total_tokens=Coalesce(Sum('tokens_used'), Value(0)),
                total_cost=Coalesce(Sum('cost'), Value(Decimal('0.0'))),
                total_requests=Coalesce(Sum('request_count'), Value(0))).order_by('-total_tokens'))
            serializer = UserModelUsageSerializer(data, many=True)
            return {"message": MODEL_USAGE_RETRIEVED_SUCCESS, "data": serializer.data}
        except Exception:
            return {"error": FAILED_TO_FETCH}


    def get_monthly_usage(self):
        try:
            data = (
                UsageLog.objects.filter(user=self.user).annotate(month=TruncMonth('created_at')).values('month', model_name=F('model__model_name')).annotate(
                total_tokens=Sum('tokens_used'), total_cost=Sum('cost')).order_by('month'))
            serializer = MonthlyUsageSerializer(data, many=True)
            return {"message": MONTHLY_USAGE_RETRIEVED_SUCCESS, "data": serializer.data}
        except Exception:
            return {"error": FAILED_TO_FETCH}

    def get_total_revenue(self):
        try:
            data = UsageLog.objects.values(model_name=F('model__model_name')).annotate(total_revenue=Coalesce(Sum('cost'), Decimal('0.0')))
            serializer = TotalRevenueSerializer(data, many=True)
            return {"message": REVENUE_RETRIEVED_SUCCESS, "data": serializer.data}
        except Exception:
            return {"error": FAILED_TO_FETCH}
        
    def get_top_user(self):
        try:
            data = (UsageLog.objects.values('user__username').annotate(
                total_cost=Coalesce(Sum('cost'), Value(Decimal('0.0'))),
                total_tokens=Coalesce(Sum('tokens_used'), Value(0)),
                total_requests=Coalesce(Sum('request_count'), Value(0))).order_by('-total_cost'))
            serializer = TopUserSerializer(data, many=True)
            return {"message": TOP_USER_RETRIEVED_SUCCESS, "data":serializer.data}
        except Exception:
            return {"error":FAILED_TO_FETCH}
        
    def get_top_model(self):
        try:
            data = (UsageLog.objects.values(model_name=F('model__model_name')).annotate(total_tokens=Sum('tokens_used')).order_by('-total_tokens')[:5])
            serializer = TopModelSerializer(data, many=True)
            return {"message":  TOP_MODEL_RETRIEVED_SUCCESS, "data": serializer.data}
        except Exception:
            return {"error": FAILED_TO_FETCH}