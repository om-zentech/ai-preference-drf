from rest_framework import serializers
from usage.models import UsageLog

class UsageLogSerializer(serializers.ModelSerializer):
    model_name = serializers.CharField(source='model.model_name', read_only=True)
    product_name = serializers.CharField(source='model.product.product_name', read_only=True)
    
    class Meta:
        model = UsageLog
        fields = '__all__'
        read_only_fields = ['user', 'cost']