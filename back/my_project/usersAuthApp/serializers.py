from rest_framework import serializers

from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
 
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth.password_validation import validate_password

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