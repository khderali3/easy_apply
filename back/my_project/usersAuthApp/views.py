from django.conf import settings


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
 
    )

from rest_framework.views import Response, status, APIView

from .serializers import (CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer, CustomUserSerializer,
                        PasswordChangeSerializer, ChangeAccountInfoSerializer, RegisterNewUserSerializer, PasswordResetConfirmSerializer
                        )


# Create your views here.
 
from rest_framework.permissions import AllowAny

 
from customCaptchaApp.utils import verify_image_captcha
from django.contrib.auth import get_user_model
from systemSettingsApp.models import MainConfiguration
from systemSettingsApp.utils import send_activation_email, send_reset_password_email
from django.db import transaction
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



from rest_framework.exceptions import ValidationError


User = get_user_model()

AUTH_COOKIE_MAX_AGE = getattr(settings, "AUTH_COOKIE_MAX_AGE", 60 * 60 * 24 * 365 * 2 )
AUTH_COOKIE_SECURE = getattr(settings, "AUTH_COOKIE_SECURE", True )
AUTH_COOKIE_HTTP_ONLY = getattr(settings, "AUTH_COOKIE_HTTP_ONLY", True )
AUTH_COOKIE_PATH = getattr(settings, "AUTH_COOKIE_PATH", '/' )
AUTH_COOKIE_SAMESITE = getattr(settings, "AUTH_COOKIE_SAMESITE", 'none' )





from djoser.social.views import ProviderAuthView
from rest_framework_simplejwt.tokens import AccessToken

from rest_framework_simplejwt.tokens import UntypedToken


class CustomProviderAuthView(ProviderAuthView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 201:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')

            response.set_cookie(
                'access',
                access_token,
                max_age=AUTH_COOKIE_MAX_AGE,
                path=AUTH_COOKIE_PATH,
                secure=AUTH_COOKIE_SECURE,
                httponly=AUTH_COOKIE_HTTP_ONLY,
                samesite=AUTH_COOKIE_SAMESITE,

            )
            response.set_cookie(
                'refresh',
                refresh_token,
                max_age=AUTH_COOKIE_MAX_AGE,
                path=AUTH_COOKIE_PATH,
                secure=AUTH_COOKIE_SECURE,
                httponly=AUTH_COOKIE_HTTP_ONLY,
                samesite=AUTH_COOKIE_SAMESITE,

            )

            try:
                token = UntypedToken(access_token)  # This validates and decodes the token
                user_id = token['user_id']  # 'user_id' is the default claim in Simple JWT
                user = User.objects.get(id=user_id)

                response.data['firstname'] = user.first_name
                response.data['lastname'] = user.last_name
                response.data['user_id'] = user.id
                response.data['is_staff'] = user.is_staff
                response.data['is_superuser'] = user.is_superuser
                response.data['permissions'] = [
                    perm for perm in user.get_all_permissions()
                    if perm.startswith('usersAuthApp.')
                ]
                response.data['groups'] = list(user.groups.values('id', 'name'))

            except :
               
                pass



 
 
        return response









class PasswordResetConfirmAPIView(APIView):
    """
    Confirms the password reset using uid and token from the link,
    and allows the user to set a new password.
    """

    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"detail": "Your password has been reset successfully."},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class SendResetPasswordEmailAPIView(APIView):
    """
    Accepts email in POST body, checks if reset can be sent based on cooldown,
    and sends the reset email using the configured template.
    """

    def post(self, request):

        is_valid, error = verify_image_captcha(request)
        if not is_valid:
            return Response({"message": error}, status=status.HTTP_400_BAD_REQUEST)



        email = request.data.get('email')
        if not email:
            return Response(
                {"detail": "Email is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        config = MainConfiguration.get_solo()

        if config.maintenance_mode:
            return Response(
                {"detail": "Password reset is temporarily unavailable due to maintenance."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        try:
            user = User.objects.get(email=email, is_active=True)
        except User.DoesNotExist:
            # Do not reveal whether the email exists
            return Response(
                {"detail": "If an account with this email exists, a reset email will be sent, [1]."},
                status=status.HTTP_200_OK
            )

        try:
            send_reset_password_email(user, request)
        except ValidationError as e:
            return Response({"detail": str(e.detail[0])}, status=status.HTTP_429_TOO_MANY_REQUESTS)
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            {"detail": "If an account with this email exists, a reset email has been sent, [2]."},
            status=status.HTTP_200_OK
        )






class ActivateAccountView(APIView):

    """
     token will be valied for one time only , if the super user mark the user not active and the user click on activation code again , it will return 
     the activation code is invalied
     
    """


    permission_classes = []  # Allow any user to activate

    def post(self, request):
 
        uidb64 = request.query_params.get('uid')
        token = request.query_params.get('token')




        if not uidb64 or not token:
            return Response({'detail': 'UID and token are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError):
            # return Response({'detail': 'Invalid user.'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'detail': 'Invalid or expired activation link (1).'}, status=status.HTTP_400_BAD_REQUEST)


        if user.is_active :
            return Response({'detail': 'Account is already activated.'}, status=status.HTTP_400_BAD_REQUEST)

        token_generator = PasswordResetTokenGenerator()
        if token_generator.check_token(user, token):
            user.is_active = True
            user.is_email_verified = True


            user.save()
            return Response({'detail': 'Account activated successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid or expired activation link (2).'}, status=status.HTTP_400_BAD_REQUEST)




class RegisterNewUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):


        is_valid, error = verify_image_captcha(request)
        if not is_valid:
            return Response({"message": error}, status=status.HTTP_400_BAD_REQUEST)



        config = MainConfiguration.get_solo()

        if config.maintenance_mode or not config.allow_user_registration:
            return Response({'detail': 'Registration is currently disabled.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = RegisterNewUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    user = serializer.save()

                    if not config.allow_registration_without_email_verification:
                        user.is_active = False
                        user.save()
                        send_activation_email(user, request)
                        return Response(
                            {'detail': 'User registered successfully. Please check your email to activate your account.'},
                            status=status.HTTP_201_CREATED
                        )
                    else:
                        user.is_active = True
                        user.save()
                        return Response(
                            {'detail': 'User registered successfully. You can now log in.'},
                            status=status.HTTP_201_CREATED
                        )

            except Exception as e:
                return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):

        is_valid, error = verify_image_captcha(request)
        if not is_valid:
            return Response({"message": error}, status=status.HTTP_400_BAD_REQUEST)


        serializer = CustomTokenObtainPairSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            # Get the tokens and other validated data
            data = serializer.validated_data

            # Generate the response including the tokens and custom data
            response = Response(data, status=status.HTTP_200_OK)

            # Set cookies for the tokens
            access_token = data.get('access')
            refresh_token = data.get('refresh')

            response.set_cookie(
                'access',
                access_token,
                max_age=AUTH_COOKIE_MAX_AGE,
                path=AUTH_COOKIE_PATH,
                secure=AUTH_COOKIE_SECURE,
                httponly=AUTH_COOKIE_HTTP_ONLY,
                samesite=AUTH_COOKIE_SAMESITE,
            )

            response.set_cookie(
                'refresh',
                refresh_token,
                max_age=AUTH_COOKIE_MAX_AGE,
                path=AUTH_COOKIE_PATH,
                secure=AUTH_COOKIE_SECURE,
                httponly=AUTH_COOKIE_HTTP_ONLY,
                samesite=AUTH_COOKIE_SAMESITE,
            )
 
 
            return response
        else:
            # If validation fails, return an error response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CustomTokenRefreshView(APIView):
    permission_classes = []  # No permissions required for this view

    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh')

        if not refresh_token:
            return Response({"detail": "Refresh token not found in cookies."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Inject the token into request data for validation
        request.data['refresh'] = refresh_token

        serializer = CustomTokenRefreshSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            access_token = serializer.validated_data['access']
            response = Response(serializer.validated_data, status=status.HTTP_200_OK)
            response.set_cookie(
                'access',
                access_token,
                max_age=AUTH_COOKIE_MAX_AGE,
                path=AUTH_COOKIE_PATH,
                secure=AUTH_COOKIE_SECURE,
                httponly=AUTH_COOKIE_HTTP_ONLY,
                samesite=AUTH_COOKIE_SAMESITE,
            )
            return response
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 

class MeView(APIView):
    def get(self, request):
        user = request.user  # The user is automatically authenticated based on the JWT token
        
        serializer = CustomUserSerializer(user, context={'request': request})

        return Response(serializer.data)

 
class LogoutView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_204_NO_CONTENT)
  
        response.delete_cookie('access')
        response.delete_cookie('refresh')

        return response




class ChangePasswordView(APIView):

    def post(self, request):
        serializer = PasswordChangeSerializer( data=request.data,   context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class ChangeAccountInfoView(APIView):
    
    def put(self, request):
        user_obj = request.user
        serializer = ChangeAccountInfoSerializer(user_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
