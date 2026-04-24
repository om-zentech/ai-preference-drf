from usage.models import UsageLog
from analytics import constants
from io import StringIO
import csv
from django.core.mail import EmailMessage

class ExportCSVService:
    def __init__(self,user):
        self.user = user
        
    def get_usage_csv(self):
        try:
            buffer = StringIO()
            writer = csv.writer(buffer)
            writer.writerow(['Model', 'Product', 'Tokens Used', 'Request Count', 'Cost', 'Created At'])
            usage_logs = UsageLog.objects.filter(user=self.user).select_related('user', 'model__product')
            for log in usage_logs:
                writer.writerow([
                    log.model.model_name,
                    log.model.product.product_name,
                    log.tokens_used,
                    log.request_count,
                    log.cost,
                    log.created_at
                ])
            buffer.seek(0)
                
            email = EmailMessage(subject=constants.EMAIL_SUBJECT, body=constants.EMAIL_BODY, to=[self.user.email],)
            email.attach(filename=constants.CSV_FILE_NAME, content=buffer.getvalue(), mimetype="text/csv")
            email.send(fail_silently=False)            
            return {"message": constants.EMAIL_SENT_SUCCESS}

        except Exception as e:
            return {"error": constants.EMAIL_SENT_FAIL}