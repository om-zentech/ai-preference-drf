from usage.models import UsageLog
from usage.serializers import UsageLogSerializer
from usage.constants import USAGE_LOG_CREATED_SUCCESS, USAGE_LOG_RETRIEVED_SUCCESS, USAGE_LOG_FAILED

class UsageLogService:

    def list_logs(self, user):
        try:
            logs = UsageLog.objects.filter(user=user)
            serializer = UsageLogSerializer(logs, many=True)
            return {"message": USAGE_LOG_RETRIEVED_SUCCESS, "data": serializer.data}
        except Exception:
            return {"error": USAGE_LOG_FAILED}

    def create_log(self, user, data):
        serializer = UsageLogSerializer(data=data)
        if not serializer.is_valid():
            return {"error": serializer.errors} 
        serializer.save(user=user)
        return {"message": USAGE_LOG_CREATED_SUCCESS, "data": serializer.data}