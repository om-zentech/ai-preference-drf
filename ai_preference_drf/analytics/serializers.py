from rest_framework import serializers

class TotalRevenueSerializer(serializers.Serializer):
    model_name = serializers.CharField()
    total_revenue = serializers.DecimalField(max_digits=12, decimal_places=4)

class TopUserSerializer(serializers.Serializer):
    username = serializers.CharField(source='user__username')
    total_cost = serializers.DecimalField(max_digits=10, decimal_places=4)
    total_tokens = serializers.IntegerField()
    total_requests = serializers.IntegerField()

class TopModelSerializer(serializers.Serializer):
    model_name = serializers.CharField()
    total_tokens = serializers.IntegerField()

class MonthlyUsageSerializer(serializers.Serializer):
    month = serializers.DateTimeField()
    model_name = serializers.CharField()
    total_tokens = serializers.IntegerField()
    total_cost = serializers.DecimalField(max_digits=12, decimal_places=4)

class UserModelUsageSerializer(serializers.Serializer):
    model_name = serializers.CharField()
    total_tokens = serializers.IntegerField()
    total_cost = serializers.DecimalField(max_digits=12, decimal_places=2)
    total_requests = serializers.IntegerField()