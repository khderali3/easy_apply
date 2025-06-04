from django.shortcuts import render
from django.conf import settings


from rest_framework_simplejwt.views import (
    TokenObtainPairView,

    
)

from rest_framework.views import Response, status, APIView

from .serializers import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer, CustomUserSerializer, PasswordChangeSerializer, ChangeAccountInfoSerializer

# Create your views here.
from rest_framework_simplejwt.tokens import AccessToken

from rest_framework.permissions import AllowAny

 
from customCaptchaApp.utils import verify_image_captcha

from django.contrib.auth import get_user_model
User = get_user_model()


 

AUTH_COOKIE_MAX_AGE = getattr(settings, "AUTH_COOKIE_MAX_AGE", 60 * 60 * 24 * 365 * 2 )
AUTH_COOKIE_SECURE = getattr(settings, "AUTH_COOKIE_SECURE", True )
AUTH_COOKIE_HTTP_ONLY = getattr(settings, "AUTH_COOKIE_HTTP_ONLY", True )
AUTH_COOKIE_PATH = getattr(settings, "AUTH_COOKIE_PATH", '/' )
AUTH_COOKIE_SAMESITE = getattr(settings, "AUTH_COOKIE_SAMESITE", 'none' )




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
