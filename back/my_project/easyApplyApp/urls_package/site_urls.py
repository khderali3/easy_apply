 
from django.contrib import admin
from django.urls import path, include

from ..views_package.site_views import (RequestServiceView, RequestAgentView, CheckRequestStatusView, GetPricesInfoView, GetAppIndexView, SpeedPackagePriceView)



urlpatterns = [
    path('request_service/', RequestServiceView.as_view() ),
    path('request_agent/', RequestAgentView.as_view() ),
    path('check_request_status/', CheckRequestStatusView.as_view() ),
    path('prices/', GetPricesInfoView.as_view() ),
    path('get_app_index/', GetAppIndexView.as_view()),

    path("speed_package_list/", SpeedPackagePriceView.as_view()) ## use for submit service request



 ]

