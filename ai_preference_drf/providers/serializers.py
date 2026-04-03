from rest_framework import serializers
from .models import Company, AIProduct, AIModel

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class AIProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIProduct
        fields = '__all__'

class AIModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIModel
        fields = '__all__'