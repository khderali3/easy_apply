 
from django.urls import path, include

urlpatterns = [
    path('site/', include('easyApplyApp.urls_package.site_urls')),
    path('staff/', include('easyApplyApp.urls_package.staff_urls'))

]