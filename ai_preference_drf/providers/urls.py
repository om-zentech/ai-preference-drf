from django.urls import path
from .views import CompanyListCreateView, AIModelListCreateView

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view()),
    path('models/', AIModelListCreateView.as_view()),
]