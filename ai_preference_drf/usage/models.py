from django.db import models

class UsageLog(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    model = models.ForeignKey('providers.AIModel', on_delete=models.CASCADE)
    tokens_used = models.IntegerField()
    request_count = models.IntegerField(default=1)
    cost = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)