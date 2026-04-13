from django.urls import path
from .views import RegisterView, LoginView, ProfileView, UserListView, PromoteUserView, DemoteUserView, DeleteProfileView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('users/', UserListView.as_view()),
    path('promote/<int:user_id>/', PromoteUserView.as_view()),
    path('demote/<int:user_id>/', DemoteUserView.as_view()),
    path('profile/delete/', DeleteProfileView.as_view()),
]