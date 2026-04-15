from django.urls import path
from .views import MonthlyUsageView, TopModelsView, TopUsersView, TotalRevenueView, UserModelUsageView, UsageLogCSVExportView

urlpatterns = [
    path('monthly/', MonthlyUsageView.as_view(), name='mothly-usage'),
    path('model-usage/', UserModelUsageView.as_view(), name='model-usage'),
    path('admin/revenue/', TotalRevenueView.as_view(), name='total-revenue'),
    path('admin/top-users/', TopUsersView.as_view(), name='top-user'),
    path('admin/top-models/', TopModelsView.as_view(), name='top-models'),
    path('export-csv/', UsageLogCSVExportView.as_view(), name='csv-export'),
]