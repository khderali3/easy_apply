



from rest_framework import serializers
from logSystemApp.models import Log
from systemSettingsApp.general_utils.custom_utils import get_user_data




 






class LogSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:
        model = Log
        fields = "__all__"
        read_only_fileds = ['id']

  

    def get_user(self, obj):
            request = self.context.get("request")  # Get request from serializer context
            return get_user_data(obj, "user", request)  # Pass request explicitly

