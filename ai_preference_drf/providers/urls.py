from django.urls import path
from .views import CompanyListCreateView, AIModelListCreateView, AIProductListCreateView, CompanyDetailView, AIProductDetailView, AIModelDetailView

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('products/', AIProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', AIProductDetailView.as_view(), name='product-details'),
    path('models/', AIModelListCreateView.as_view(), name='model-list-create'),
    path('models/<int:pk>/', AIModelDetailView.as_view(), name='model-detail'),
]