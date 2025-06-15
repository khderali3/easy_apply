
from rest_framework.views import APIView, status, Response


from ..serializers_package.site_serializer import (RequestAgentSerializer, RequestServiceSerializer, CheckRequestStatusSerializer, SpeedPackagePriceSerializer,
                                                    UnlimitedSpeedTrafficPackagePriceSerializer , TrafficPackagePriceSerializer ,                                  
                                                    CardLabelCheckRequestSerializer, CardLabelRequestAgentSerializer, CardLabelRequestServiceSerializer,
                                                    CardLabelServicePricesServiceSerializer,  AppPricesTitleSerializer, 
                                                    AppSettingSerializer

                                                   )


from ..models import (RequestAgent, RequestService, SpeedPackagePrice, UnlimitedSpeedTrafficPackagePrice, TrafficPackagePrice,
                    CardLabelCheckRequest, CardLabelRequestAgent, CardLabelRequestService, CardLabelServicePrices, 
                    AppPricesTitle, AppSetting, 
                    )


from rest_framework.permissions import AllowAny

from django.shortcuts import get_object_or_404

 



from systemSettingsApp.general_utils.custom_utils import get_client_ip






from customCaptchaApp.utils import verify_image_captcha

from systemSettingsApp.models import MainConfiguration

import json





class SpeedPackagePriceView(APIView):
    permission_classes = []
    def get(self, request):
        speed_packages = SpeedPackagePrice.objects.all()
        serailizer = SpeedPackagePriceSerializer(speed_packages, many=True)
        return Response(serailizer.data, status=status.HTTP_200_OK)






 

class GetAppIndexView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # return Response({'message' : "error from django"}, status=status.HTTP_400_BAD_REQUEST)

        app_index_title_obj = AppSetting.get_solo()
        main_config = MainConfiguration.get_solo()
        compoany_logo = None
        try:
            if main_config.company_logo:
                compoany_logo = request.build_absolute_uri(main_config.company_logo.url)  # full absolute URL
        except:
            pass


        key = request.query_params.get("q")

        if key:
            if key == "card_check_request_label":
                card_check_request_label_obj = CardLabelCheckRequest.get_solo()
                return Response({
                    "card_check_request_label" : CardLabelCheckRequestSerializer(card_check_request_label_obj).data,
                    "compoany_logo" : compoany_logo,
                    "app_index_title" : AppSettingSerializer(app_index_title_obj).data

                }, status=status.HTTP_200_OK)
 
            elif key == "card_request_agent_label":
                card_request_agent_label_obj = CardLabelRequestAgent.get_solo()
                return Response({
                "card_request_agent_label" : CardLabelRequestAgentSerializer(card_request_agent_label_obj).data,
                "compoany_logo" : compoany_logo,
                "app_index_title" : AppSettingSerializer(app_index_title_obj).data
                }, status=status.HTTP_200_OK)

            elif key == "card_request_service_label":
                card_request_service_label_obj = CardLabelRequestService.get_solo()
                return Response({
                "card_request_service_label" : CardLabelRequestServiceSerializer(card_request_service_label_obj).data,
                "compoany_logo" : compoany_logo,
                "app_index_title" : AppSettingSerializer(app_index_title_obj).data

                }, status=status.HTTP_200_OK)

            elif key == "card_service_prices_label":
                card_service_prices_label_obj = CardLabelServicePrices.get_solo()
                return Response({
                "card_service_prices_label" : CardLabelServicePricesServiceSerializer(card_service_prices_label_obj).data,
                "compoany_logo" : compoany_logo,
                "app_index_title" : AppSettingSerializer(app_index_title_obj).data

                }, status=status.HTTP_200_OK)

            else:
                return Response({'message' : 'your key is invalied!'}, status=status.HTTP_400_BAD_REQUEST)


        card_check_request_label_obj = CardLabelCheckRequest.get_solo()
        card_request_agent_label_obj = CardLabelRequestAgent.get_solo()
        card_request_service_label_obj = CardLabelRequestService.get_solo()
        card_service_prices_label_obj = CardLabelServicePrices.get_solo()

        return Response({
            "compoany_logo" : compoany_logo,
            "app_index_title" : AppSettingSerializer(app_index_title_obj).data,
            "card_check_request_label" : CardLabelCheckRequestSerializer(card_check_request_label_obj).data,
            "card_request_agent_label" : CardLabelRequestAgentSerializer(card_request_agent_label_obj).data,
            "card_request_service_label" : CardLabelRequestServiceSerializer(card_request_service_label_obj).data,
            "card_service_prices_label" : CardLabelServicePricesServiceSerializer(card_service_prices_label_obj).data,

        }, status=status.HTTP_200_OK)



 
class GetPricesInfoView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        app_prices_title_obj = AppPricesTitle.get_solo()
        main_config = MainConfiguration.get_solo()
        compoany_logo = None
        try:
            if main_config.company_logo:
                compoany_logo = request.build_absolute_uri(main_config.company_logo.url)  # full absolute URL
        except:
            pass





        unlimited_speed_packages = UnlimitedSpeedTrafficPackagePrice.objects.all()
        traffic_packages = TrafficPackagePrice.objects.all()
        speed_packages = SpeedPackagePrice.objects.all()

        data = {
            "compoany_logo" : compoany_logo,
            "app_prices_title" : AppPricesTitleSerializer(app_prices_title_obj).data,
            "unlimited_speed_packages": UnlimitedSpeedTrafficPackagePriceSerializer(unlimited_speed_packages, many=True).data,
            "traffic_packages": TrafficPackagePriceSerializer(traffic_packages, many=True).data,
            "speed_packages": SpeedPackagePriceSerializer(speed_packages, many=True).data,
        }

        # serializer = GetPricesInfoSerializer(data)
        # return Response(serializer.data)
        return Response(data)






class RequestServiceView(APIView):
    permission_classes = [AllowAny]
 
    def post(self, request):


        is_valid, error = verify_image_captcha(request)
        if not is_valid:
            return Response({"message": error}, status=status.HTTP_400_BAD_REQUEST)
        

        settings = AppSetting.get_solo()
        max_allowed = settings.max_request_user_service

        phone_number = request.data.get("phone_number")
        if not phone_number:
            return Response({"message": "Phone number is required."}, status=status.HTTP_400_BAD_REQUEST)

        request_count = RequestService.objects.filter(phone_number=phone_number).count()
        if max_allowed and request_count >= max_allowed:
            return Response(
                {"message": f"You are not allowed to send more than {max_allowed} requests."},
                status=status.HTTP_403_FORBIDDEN
            )






        speed_obj_id = request.data.get('speed_package')
        speed_obj = get_object_or_404(SpeedPackagePrice, id=speed_obj_id)

        speed_obj_json = json.dumps(SpeedPackagePriceSerializer(speed_obj).data)
        data = request.data.copy()
        data['speed_package'] = speed_obj_json

        data['created_ip_address']  = get_client_ip(request)

        serializer = RequestServiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class RequestAgentView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
 
        is_valid, error = verify_image_captcha(request)
        if not is_valid:
            return Response({"message": error}, status=status.HTTP_400_BAD_REQUEST)



        settings = AppSetting.get_solo()
        max_allowed = settings.max_request_agent

        phone_number = request.data.get("phone_number")
        if not phone_number:
            return Response({"message": "Phone number is required."}, status=status.HTTP_400_BAD_REQUEST)

        request_count = RequestService.objects.filter(phone_number=phone_number).count()
        if max_allowed and request_count >= max_allowed:
            return Response(
                {"message": f"You are not allowed to send more than {max_allowed} requests."},
                status=status.HTTP_403_FORBIDDEN
            )










        data = request.data.copy()
        data['created_ip_address']  = get_client_ip(request)


        serializer = RequestAgentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CheckRequestStatusView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):


        is_valid, error = verify_image_captcha(request)
        if not is_valid:
            return Response({"message": error}, status=status.HTTP_400_BAD_REQUEST)



        check_request_serializer = CheckRequestStatusSerializer(data=request.data)
        if not check_request_serializer.is_valid():
            return Response(check_request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        type_of_request = check_request_serializer.validated_data['type_of_request']
        phone_number = check_request_serializer.validated_data['phone_number']

        serializer = None
 
        if type_of_request == 'client':
            queryset = RequestService.objects.filter(phone_number=phone_number)
            serializer = RequestServiceSerializer(queryset, many=True)
        elif type_of_request == 'agent':  # type_of_request == 'agent'
            queryset = RequestAgent.objects.filter(phone_number=phone_number)
            serializer = RequestAgentSerializer(queryset, many=True)

        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)

        else :
            return Response({"message": "type_of_request is incurrct"}, status=status.HTTP_400_BAD_REQUEST)
