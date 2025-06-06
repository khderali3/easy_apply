from rest_framework import serializers

from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
 
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth.password_validation import validate_password




from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from rest_framework.exceptions import ValidationError

User = get_user_model()
token_generator = PasswordResetTokenGenerator()

from rest_framework_simplejwt.tokens import RefreshToken



class CustomProviderTokenStrategy:

    """
    this only to add extra att in refresh token , but if you wana add extra att to a full resupose add from view .
    """

    @classmethod
    def obtain(cls, user):

        refresh = RefreshToken.for_user(user)

        refresh['first_name'] = user.first_name
        refresh['is_staff'] = user.is_staff
        refresh['is_superuser'] = user.is_superuser
        refresh['custom_att'] = "custom_value"

 
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
 
          }

 

 



class PasswordResetConfirmSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, min_length=8)
    confirm_new_password = serializers.CharField(write_only=True, min_length=8)

    def validate(self, data):
        # Validate matching passwords
        if data["new_password"] != data["confirm_new_password"]:
            raise ValidationError({"confirm_new_password": "Passwords do not match."})

        # Decode UID and fetch user
        try:
            uid = force_str(urlsafe_base64_decode(data["uid"]))
            user = User.objects.get(pk=uid, is_active=True)
        except (User.DoesNotExist, ValueError, TypeError, OverflowError):
            raise ValidationError({"uid": "Invalid or expired reset link."})

        # Validate token
        if not token_generator.check_token(user, data["token"]):
            raise ValidationError({"token": "Invalid or expired reset link."})

        self.user = user
        return data

    def save(self, **kwargs):
        password = self.validated_data["new_password"]
        self.user.set_password(password)
        # self.user.last_password_reset_email_sent = None  # Clear cooldown after reset
        self.user.is_email_verified = True

        self.user.save()








 
class RegisterNewUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8, label="Confirm password")

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'password2']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already registered.")
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user













# used for Loing
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        # Custom validation logic, for example, check if the user is active
        data = super().validate(attrs)
        user = get_user_model().objects.get(email=attrs['email'])
        
        if not user.is_active:
            raise serializers.ValidationError('User account is not active.')

        # Add any extra claims if necessary
        data['firstname'] = user.first_name  
        data['lastname'] = user.last_name   
        data['user_id'] = user.id 

        data['is_staff'] = user.is_staff   
        data['is_superuser'] = user.is_superuser  

        data['permissions'] = [
                perm for perm in user.get_all_permissions()
                if perm.startswith('usersAuthApp.')
            ]

        data['groups'] = list(user.groups.values('id', 'name'))
   
        return data







# used for refresh token
class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        # Call the parent validation method
        data = super().validate(attrs)
        
        # Example: Add custom fields to the response
        data['message'] = "Token successfully refreshed."
        
        if self.context['request'].user.is_authenticated:
            user = self.context['request'].user
        
            # Add any extra claims if necessary
            data['firstname'] = user.first_name  
            data['lastname'] = user.last_name   
            data['user_id'] = user.id 

            data['is_staff'] = user.is_staff   
            data['is_superuser'] = user.is_superuser  

            data['permissions'] = [
                    perm for perm in user.get_all_permissions()
                    if perm.startswith('usersAuthApp.')
                ]

            data['groups'] = list(user.groups.values('id', 'name'))
   
        return data







## used for /me
class CustomUserSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()
    permissions = serializers.SerializerMethodField()


    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_staff','is_superuser',  'groups', 'permissions']  # Add any other fields

 
    
    def get_groups(self, obj):
        # Get the groups for the user and return a list of dictionaries with group id and name
        groups = obj.groups.all()
        return [{'id': group.id, 'name': group.name} for group in groups]

    def get_permissions(self, obj):
 
        permissions = [   perm for perm in obj.get_all_permissions()   if perm.startswith('usersAuthApp.')  ]
        return permissions

 





class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = self.context.get('request').user  # Get the authenticated user from the request
        
        # Check if the old password is correct
        if not user.check_password(data['old_password']):
            raise serializers.ValidationError({"old_password": "Old password is incorrect."})

        # Check if the new password and confirm password match
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "New passwords do not match."})

        return data

    def save(self):
        user = self.context.get('request').user  # Get the authenticated user from the request
        new_password = self.validated_data['new_password']
        user.set_password(new_password)  # Set the new password
        user.save()  # Save the user with the new password
        return user




 
class ChangeAccountInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'country','city', 'address', 'phone_number', 'email_notifications_enabled' ]