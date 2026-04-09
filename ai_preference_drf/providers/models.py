from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.company_name

class AIProduct(models.Model):
    product_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name

class AIModel(models.Model):
    model_name = models.CharField(max_length=100)
    product = models.ForeignKey(AIProduct, on_delete=models.CASCADE)
    price_per_1k_tokens = models.DecimalField(max_digits=10, decimal_places=4)  
    
    def __str__(self):
        return self.model_name