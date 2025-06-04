 
from django.contrib import admin
from django.urls import path, include


from ..views_package.staff_views import (RequestServiceView, RequestAgentView, RequestServicePrivateNoteView,
                                         RequestAgentPrivateNoteView,SpeedPackagePriceView, TrafficPackagePriceView,
                                         UnlimitedSpeedTrafficPackagePriceView
                                         
                                         )



urlpatterns = [
    path('request_service/', RequestServiceView.as_view()),
    path('request_service/<int:id>/', RequestServiceView.as_view()),

    path('request_service/<int:request_id>/note/', RequestServicePrivateNoteView.as_view()),
    path('request_service/<int:request_id>/note/<int:id>/', RequestServicePrivateNoteView.as_view()),



    path('request_agent/', RequestAgentView.as_view()),
    path('request_agent/<int:id>/', RequestAgentView.as_view()),



    path('request_agent/<int:request_id>/note/', RequestAgentPrivateNoteView.as_view()),
    path('request_agent/<int:request_id>/note/<int:id>/', RequestAgentPrivateNoteView.as_view()),


    path('speed_package_price/', SpeedPackagePriceView.as_view()),
    path('speed_package_price/<int:id>/', SpeedPackagePriceView.as_view()),


    path('traffic_package_price/', TrafficPackagePriceView.as_view()),
    path('traffic_package_price/<int:id>/', TrafficPackagePriceView.as_view()),


    path('unlimited_speed_traffic_package_price/', UnlimitedSpeedTrafficPackagePriceView.as_view()),
    path('unlimited_speed_traffic_package_price/<int:id>/', UnlimitedSpeedTrafficPackagePriceView.as_view()),


]