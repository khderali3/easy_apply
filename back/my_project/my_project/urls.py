 
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/easyApplyApp/', include('easyApplyApp.urls')),
    path('api/captcha/', include('customCaptchaApp.urls')),
    path('api/users_auth_app/', include('usersAuthApp.urls')),
    path('api/users_managment_app/', include('usersManagmentApp.urls')),
    path('api/logSystemApp/', include('logSystemApp.urls')),
    path('api/systemSettingsApp/', include('systemSettingsApp.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)