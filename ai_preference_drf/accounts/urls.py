from django.urls import path
from .views import RegisterView, LoginView, ProfileView, UserListView, PromoteUserView, DemoteUserView, DeleteProfileView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view()),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('promote/<int:user_id>/', PromoteUserView.as_view(), name='promote-user'),
    path('demote/<int:user_id>/', DemoteUserView.as_view(), name='demote-user'),
    path('profile/delete/', DeleteProfileView.as_view(), name='delete'),
]