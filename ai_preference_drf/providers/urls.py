from django.urls import path
from .views import CompanyListCreateView, AIModelListCreateView, AIProductListCreateView, CompanyDetailView, AIProductDetailView, AIModelDetailView

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view()),
    path('companies/<int:pk>/', CompanyDetailView.as_view()),
    path('products/', AIProductListCreateView.as_view()),
    path('products/<int:pk>/', AIProductDetailView.as_view()),
    path('models/', AIModelListCreateView.as_view()),
    path('models/<int:pk>/', AIModelDetailView.as_view()),
]