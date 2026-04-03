from django.urls import path
from .views import UsageLogView

urlpatterns = [
    path('', UsageLogView.as_view()),
]