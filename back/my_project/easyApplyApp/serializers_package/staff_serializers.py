from ..models import (RequestService, RequestAgent,
                    RequestServicePrivateNote, RequestAgentPrivateNote,
                    SpeedPackagePrice,TrafficPackagePrice, UnlimitedSpeedTrafficPackagePrice
                    )


from rest_framework import serializers

# from ..utils import get_user_data

from systemSettingsApp.general_utils.custom_utils import get_user_data




class UnlimitedSpeedTrafficPackagePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnlimitedSpeedTrafficPackagePrice
        fields = "__all__"
        read_only_fields = ["id"]





class TrafficPackagePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficPackagePrice
        fields = "__all__"
        read_only_fields = ["id"]




class SpeedPackagePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeedPackagePrice
        fields = "__all__"
        read_only_fields = ["id"]


class RequestAgentPrivateNoteSerializer(serializers.ModelSerializer):
    user_info = serializers.SerializerMethodField()
    
    class Meta:
        model = RequestAgentPrivateNote
        fields = "__all__"
        read_only_fields = ["id"]

    def get_user_info(self, obj):
        return get_user_data(obj, "user")  
    

class RequestServicePrivateNoteSerializer(serializers.ModelSerializer):
    user_info = serializers.SerializerMethodField()
    class Meta:
        model = RequestServicePrivateNote
        fields = "__all__"
        read_only_fields = ["id", 'user', 'created_ip_address']

    def get_user_info(self, obj):
        return get_user_data(obj, "user")  



class RequestAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestAgent
        fields = "__all__"
        read_only_fields = ["id", 'created_ip_address']

class RequestServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestService
        fields = "__all__"
        read_only_fields = ["id", "created_ip_address"]








