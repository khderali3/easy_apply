 
from django.urls import path, re_path

from .views import (LoginView, CustomTokenRefreshView, MeView, LogoutView, ChangePasswordView,
                     ChangeAccountInfoView, RegisterNewUserView, ActivateAccountView, SendResetPasswordEmailAPIView, PasswordResetConfirmAPIView,
                     CustomProviderAuthView
                     
                     )





urlpatterns = [

 
    path('o/<str:provider>/', CustomProviderAuthView.as_view(), name='djoser-provider-auth'),


    path('register/', RegisterNewUserView.as_view() ),
    path('activate_account/', ActivateAccountView.as_view() ),

    path('request_reset_password/', SendResetPasswordEmailAPIView.as_view() ),
    path('confirm_reset_password/', PasswordResetConfirmAPIView.as_view() ),


    path('login/', LoginView.as_view() ),
    path('refresh_token/', CustomTokenRefreshView.as_view()),
    path('me/', MeView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('change_account_info/', ChangeAccountInfoView.as_view())

    
]


