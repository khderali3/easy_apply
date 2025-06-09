


from rest_framework import serializers



from .models import MainConfiguration, QueuedEmail


class MainConfigurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainConfiguration
        fields = "__all__"
        read_only_fields = ['id', "created_at", "updated_at" ]

 
 
class QueuedEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = QueuedEmail
        fields = "__all__"
        read_only_fields = ["id"]