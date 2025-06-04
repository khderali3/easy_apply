
from rest_framework.views import APIView, status, Response


from ..serializers_package.site_serializer import (RequestAgentSerializer, RequestServiceSerializer, CheckRequestStatusSerializer, SpeedPackagePriceSerializer,
                                                    GetPricesInfoSerializer , UnlimitedSpeedTrafficPackagePriceSerializer , TrafficPackagePriceSerializer                                   

                                                   )


from ..models import RequestAgent, RequestService, SpeedPackagePrice, UnlimitedSpeedTrafficPackagePrice, TrafficPackagePrice


from rest_framework.permissions import AllowAny

from django.shortcuts import get_object_or_404

from ..utils import get_client_ip

from customCaptchaApp.utils import verify_image_captcha



import json




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

