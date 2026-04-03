from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class AIProduct(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class AIModel(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(AIProduct, on_delete=models.CASCADE)
    price_per_1k_tokens = models.DecimalField(max_digits=10, decimal_places=4)  
    
    def __str__(self):
        return self.name