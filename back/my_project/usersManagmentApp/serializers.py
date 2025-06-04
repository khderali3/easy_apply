
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
User = get_user_model()




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email',
                  'is_active', 'is_staff', 'is_superuser' ,'is_email_verified', 'email_notifications_enabled',
                  'created_date', 'updated_date'
                ]    
        
        read_only_fields = ['is_email_verified','created_date', 'updated_date']




class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User

        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'confirm_password',
                  'is_active', 'is_staff', 'is_superuser' ,'is_email_verified', 'email_notifications_enabled'
                ]    

 
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['id' ]

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.pop('confirm_password')

        # Check if password and confirm password match
        if password != confirm_password:
            raise serializers.ValidationError({"confirm_password": "Password fields must match."})
        
        if len(password) < 8:
            raise serializers.ValidationError({"password": "Password must be at least 8 characters long."})

        

        return attrs

    def create(self, validated_data):
        # Create the user using the create_user method (which hashes the password)
        user = User.objects.create_user(**validated_data)
        return user




class SetUserPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, required=True, min_length=8)
    re_new_password = serializers.CharField(write_only=True, required=True, min_length=8)

    def validate(self, data):
        if data['new_password'] != data['re_new_password']:
            raise serializers.ValidationError({'re_new_password': 'Passwords do not match.'})
        
        return data




 

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"
        read_only_fields = ['id' ]



class GroupSerializer(serializers.ModelSerializer):

    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = "__all__"
        read_only_fields = ['id', 'permissions' ]