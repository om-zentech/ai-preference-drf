from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import UsageLog
from .serializers import UsageLogSerializer

class UsageLogView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logs = UsageLog.objects.filter(user=request.user)
        serializer = UsageLogSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsageLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)