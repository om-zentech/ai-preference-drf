from django.contrib import admin
from providers.models import Company, AIModel, AIProduct

admin.site.register(Company)
admin.site.register(AIProduct)
admin.site.register(AIModel)
