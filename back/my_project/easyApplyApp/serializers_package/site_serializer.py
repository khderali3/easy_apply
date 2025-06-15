
from ..models import (RequestService, RequestAgent,
                       SpeedPackagePrice, TrafficPackagePrice, UnlimitedSpeedTrafficPackagePrice,
                       CardLabelCheckRequest, CardLabelRequestAgent, CardLabelRequestService, CardLabelServicePrices, 
                        AppPricesTitle, AppSetting

                      )

from rest_framework import serializers
 


class AppSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppSetting
        fields = "__all__"
        read_only_fields = ["id"]


class AppPricesTitleSerializer(serializers.ModelSerializer):


    class Meta:
        model = AppPricesTitle
        fields = "__all__"
        read_only_fields = ["id"]



 


class CardLabelCheckRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardLabelCheckRequest
        fields = "__all__"
        read_only_fields = ["id"]





class CardLabelRequestAgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardLabelRequestAgent
        fields = "__all__"
        read_only_fields = ["id"]

class CardLabelRequestServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardLabelRequestService
        fields = "__all__"
        read_only_fields = ["id"]



class CardLabelServicePricesServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardLabelServicePrices
        fields = "__all__"
        read_only_fields = ["id"]













class UnlimitedSpeedTrafficPackagePriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnlimitedSpeedTrafficPackagePrice
        fields = "__all__"
        read_only_fields = ['id']





class TrafficPackagePriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrafficPackagePrice
        fields = "__all__"
        read_only_fields = ['id']





class SpeedPackagePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeedPackagePrice
        fields =  "__all__"



class RequestServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestService
        fields = "__all__"
        read_only_fields = ['id']


 


class RequestAgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestAgent
        fields = "__all__"
        read_only_fields = ['id']








class CheckRequestStatusSerializer(serializers.Serializer):
    TYPE_CHOICES = (
        ('agent', 'Agent'),
        ('client', 'Client'),
    )

    type_of_request = serializers.ChoiceField(choices=TYPE_CHOICES)
    phone_number = serializers.CharField(max_length=20)
 



