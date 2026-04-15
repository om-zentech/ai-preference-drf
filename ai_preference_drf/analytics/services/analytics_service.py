from usage.models import UsageLog
from decimal import Decimal
from django.db.models.functions import Coalesce, TruncMonth
from django.db.models import Sum, F, Value

class AnalyticsService:
    def __init__(self, user):
        self.user = user
    def get_user_model_usage(self):
        return (
            UsageLog.objects.filter(user=self.user).values(model_name=F('model__model_name')).annotate(
                total_tokens=Coalesce(Sum('tokens_used'), Value(0)),
                total_cost=Coalesce(Sum('cost'), Value(Decimal('0.0'))),
                total_requests=Coalesce(Sum('request_count'), Value(0))).order_by('-total_tokens'))
    
    def get_monthly_usage(self):
        return (
            UsageLog.objects.filter(user=self.user).annotate(month=TruncMonth('created_at')).values('month', 'model__model_name').annotate(
                total_tokens=Sum('tokens_used'), total_cost=Sum('cost')).order_by('month')
        )
        
    