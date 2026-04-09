from django.db.models.signals import pre_save
from django.dispatch import receiver
from decimal import Decimal
from .models import UsageLog

@receiver(pre_save, sender=UsageLog)
def calculate_cost(sender, instance, **kwargs):
    if instance.model and instance.tokens_used:
        price = instance.model.price_per_1k_tokens

        tokens = Decimal(instance.tokens_used)
        instance.cost = (tokens / Decimal('1000')) * price