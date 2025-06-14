


from rest_framework import serializers



from .models import MainConfiguration, QueuedEmail



class SiteSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainConfiguration
        fields = ["email_service_enabled", "is_captcha_enabled", "maintenance_mode", "allow_user_registration", "allow_registration_without_email_verification"]
 



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