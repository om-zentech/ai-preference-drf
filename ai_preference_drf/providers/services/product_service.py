from providers.models import AIProduct
from providers.serializers import AIProductSerializer
from providers.constants import PRODUCT_RETRIEVED_FAILED, PRODUCT_RETRIEVED_SUCCESS, PRODUCT_CREATED_SUCCESS, PRODUCT_NOT_FOUND

class AIProductService:

    def list_products(self):
        try:
            products = AIProduct.objects.all()
            serializer = AIProductSerializer(products, many=True)
            return {"message": PRODUCT_RETRIEVED_SUCCESS, "data": serializer.data}
        except Exception:
            return {"error": PRODUCT_RETRIEVED_FAILED}

    def create_product(self, data):
        serializer = AIProductSerializer(data=data)

        if not serializer.is_valid():
            return {"error": serializer.errors}

        serializer.save()
        return {"message":PRODUCT_CREATED_SUCCESS, "data": serializer.data}
    
    def get_product(self, pk):
        try:
            product = AIProduct.objects.get(pk=pk)
        except AIProduct.DoesNotExist:
            return {"error": PRODUCT_NOT_FOUND}

        serializer = AIProductSerializer(product)
        return {"data": serializer.data}

    def update_product(self, pk, data):
        try:
            product = AIProduct.objects.get(pk=pk)
        except AIProduct.DoesNotExist:
            return {"error": PRODUCT_NOT_FOUND}

        serializer = AIProductSerializer(product, data=data, partial=True)

        if not serializer.is_valid():
            return {"error": serializer.errors}

        serializer.save()
        return {"data": serializer.data}