from django.urls import path
from .views import CompanyListCreateView, AIModelListCreateView, AIProductListCreateView

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view()),
    path('products/', AIProductListCreateView.as_view()),
    path('models/', AIModelListCreateView.as_view()),
]