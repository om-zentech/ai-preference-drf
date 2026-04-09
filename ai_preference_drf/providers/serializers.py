from rest_framework import serializers
from .models import Company, AIProduct, AIModel

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class AIProductSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.company_name', read_only=True)
    
    class Meta:
        model = AIProduct
        fields = '__all__'

class AIModelSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name', read_only=True)
 
    class Meta:
        model = AIModel
        fields = '__all__'