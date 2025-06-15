 
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from django.http import JsonResponse
from django.conf.urls import handler404
from rest_framework.views import APIView, Response, status

 
def custom_404_handler(request, exception):
    return JsonResponse(
        {
            "message": f"Request path not found: {request.path}"
        },
        status=404
    )

 

handler404 = custom_404_handler


class  Custom404DevelopmentView(APIView):
    permission_classes = []
    def get(self, request):
        return Response(
            {
                "message": f"Request path not found (development): {request.path}"
            },
            status=404
        )


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
    urlpatterns += [
        re_path(r'^.*$', Custom404DevelopmentView.as_view()),
    ]

 