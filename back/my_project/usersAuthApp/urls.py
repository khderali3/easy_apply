 
from django.urls import path, include

from .views import LoginView, CustomTokenRefreshView, MeView, LogoutView, ChangePasswordView, ChangeAccountInfoView

urlpatterns = [
    path('login/', LoginView.as_view() ),
    path('refresh_token/', CustomTokenRefreshView.as_view()),
    path('me/', MeView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('change_account_info/', ChangeAccountInfoView.as_view())
]


