
from rest_framework.views import APIView, status, Response


from ..serializers_package.site_serializer import (RequestAgentSerializer, RequestServiceSerializer, CheckRequestStatusSerializer, SpeedPackagePriceSerializer,
                                                    GetPricesInfoSerializer , UnlimitedSpeedTrafficPackagePriceSerializer , TrafficPackagePriceSerializer ,                                  
                                                    CardLabelCheckRequestSerializer, CardLabelRequestAgentSerializer, CardLabelRequestServiceSerializer,
                                                    CardLabelServicePricesServiceSerializer, AppIndexTitleSerializer

                                                   )


from ..models import (RequestAgent, RequestService, SpeedPackagePrice, UnlimitedSpeedTrafficPackagePrice, TrafficPackagePrice,
                    CardLabelCheckRequest, CardLabelRequestAgent, CardLabelRequestService, CardLabelServicePrices, AppIndexTitle
                     
                    )


from rest_framework.permissions import AllowAny

from django.shortcuts import get_object_or_404

 



from systemSettingsApp.general_utils.custom_utils import get_client_ip






from customCaptchaApp.utils import verify_image_captcha

from systemSettingsApp.models import MainConfiguration

import json




class GetAppIndexView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # return Response({'message' : "error from django"}, status=status.HTTP_400_BAD_REQUEST)

        app_index_title_obj = AppIndexTitle.get_solo()
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
                    "app_index_title" : AppIndexTitleSerializer(app_index_title_obj).data

                }, status=status.HTTP_200_OK)
 
            elif key == "card_request_agent_label":
                card_request_agent_label_obj = CardLabelRequestAgent.get_solo()
                return Response({
                "card_request_agent_label" : CardLabelRequestAgentSerializer(card_request_agent_label_obj).data,
                "compoany_logo" : compoany_logo,
                "app_index_title" : AppIndexTitleSerializer(app_index_title_obj).data
                }, status=status.HTTP_200_OK)

            elif key == "card_request_service_label":
                card_request_service_label_obj = CardLabelRequestService.get_solo()
                return Response({
                "card_request_service_label" : CardLabelRequestServiceSerializer(card_request_service_label_obj).data,
                "compoany_logo" : compoany_logo,
                "app_index_title" : AppIndexTitleSerializer(app_index_title_obj).data

                }, status=status.HTTP_200_OK)

            elif key == "card_service_prices_label":
                card_service_prices_label_obj = CardLabelServicePrices.get_solo()
                return Response({
                "card_service_prices_label" : CardLabelServicePricesServiceSerializer(card_service_prices_label_obj).data,
                "compoany_logo" : compoany_logo,
                "app_index_title" : AppIndexTitleSerializer(app_index_title_obj).data

                }, status=status.HTTP_200_OK)

            else:
                return Response({'message' : 'your key is invalied!'}, status=status.HTTP_400_BAD_REQUEST)


        card_check_request_label_obj = CardLabelCheckRequest.get_solo()
        card_request_agent_label_obj = CardLabelRequestAgent.get_solo()
        card_request_service_label_obj = CardLabelRequestService.get_solo()
        card_service_prices_label_obj = CardLabelServicePrices.get_solo()

        return Response({
            "compoany_logo" : compoany_logo,
            "app_index_title" : AppIndexTitleSerializer(app_index_title_obj).data,
            "card_check_request_label" : CardLabelCheckRequestSerializer(card_check_request_label_obj).data,
            "card_request_agent_label" : CardLabelRequestAgentSerializer(card_request_agent_label_obj).data,
            "card_request_service_label" : CardLabelRequestServiceSerializer(card_request_service_label_obj).data,
            "card_service_prices_label" : CardLabelServicePricesServiceSerializer(card_service_prices_label_obj).data,

        }, status=status.HTTP_200_OK)



 
class GetPricesInfoView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        unlimited_speed_packages = UnlimitedSpeedTrafficPackagePrice.objects.all()
        traffic_packages = TrafficPackagePrice.objects.all()
        speed_packages = SpeedPackagePrice.objects.all()

        data = {
            "unlimited_speed_packages": UnlimitedSpeedTrafficPackagePriceSerializer(unlimited_speed_packages, many=True).data,
            "traffic_packages": TrafficPackagePriceSerializer(traffic_packages, many=True).data,
            "speed_packages": SpeedPackagePriceSerializer(speed_packages, many=True).data,
        }

        serializer = GetPricesInfoSerializer(data)
        return Response(serializer.data)






class RequestServiceView(APIView):
    permission_classes = [AllowAny]
 
    def post(self, request):


        is_valid, error = verify_image_captcha(request)
        if not is_valid:
            return Response({"message": error}, status=status.HTTP_400_BAD_REQUEST)




        speed_obj_id = request.data.get('speed')
        speed_obj = get_object_or_404(SpeedPackagePrice, id=speed_obj_id)
        speed_json = json.dumps(SpeedPackagePriceSerializer(speed_obj).data)
        data = request.data.copy()
        data['speed'] = speed_json
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


 
        if type_of_request == 'client':
            queryset = RequestService.objects.filter(phone_number=phone_number)
            serializer = RequestServiceSerializer(queryset, many=True)
        else:  # type_of_request == 'agent'
            queryset = RequestAgent.objects.filter(phone_number=phone_number)
            serializer = RequestAgentSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

