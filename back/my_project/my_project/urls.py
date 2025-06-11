 
from django.contrib import admin
from django.urls import path, include
 




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/easyApplyApp/', include('easyApplyApp.urls')),
    path('api/captcha/', include('customCaptchaApp.urls')),
    path('api/users_auth_app/', include('usersAuthApp.urls')),
    path('api/users_managment_app/', include('usersManagmentApp.urls')),
    path('api/logSystemApp/', include('logSystemApp.urls')),
    path('api/systemSettingsApp/', include('systemSettingsApp.urls')),
]
