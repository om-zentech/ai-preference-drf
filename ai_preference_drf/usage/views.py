from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from usage.services.usage_service import UsageLogService

class UsageLogView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = UsageLogService()
        result = service.list_logs(request.user)

        if "error" in result:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        service = UsageLogService()
        result = service.create_log(request.user, request.data)

        if "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_201_CREATED)