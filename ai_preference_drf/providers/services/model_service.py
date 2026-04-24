from providers.models import AIModel
from providers.serializers import AIModelSerializer
from providers.constants import MODEL_RETRIEVED_SUCCESS, MODEL_RETRIEVED_FAILED, MODEL_CREATED_SUCCESS, MODEL_NOT_FOUND

class AIModelService:

    def list_models(self):
        try:
            models = AIModel.objects.all()
            serializer = AIModelSerializer(models, many=True)

            return {"message": MODEL_RETRIEVED_SUCCESS, "data": serializer.data}

        except Exception:
            return {"error": MODEL_RETRIEVED_FAILED}

    def create_model(self, data):
        serializer = AIModelSerializer(data=data)

        if not serializer.is_valid():
            return {"error": serializer.errors}

        serializer.save()
        return {"message": MODEL_CREATED_SUCCESS, "data": serializer.dat }

    def get_model(self, pk):
        try:
            model = AIModel.objects.get(pk=pk)
        except AIModel.DoesNotExist:
            return {"error": MODEL_NOT_FOUND}

        serializer = AIModelSerializer(model)
        return {"data": serializer.data}

    def update_model(self, pk, data):
        try:
            model = AIModel.objects.get(pk=pk)
        except AIModel.DoesNotExist:
            return {"error": MODEL_NOT_FOUND}

        serializer = AIModelSerializer(model, data=data, partial=True)

        if not serializer.is_valid():
            return {"error": serializer.errors}

        serializer.save()
        return {"data": serializer.data}