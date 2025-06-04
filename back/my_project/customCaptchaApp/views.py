import uuid
import random
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from redis.exceptions import ConnectionError  # from redis-py package




import uuid
import base64
from io import BytesIO
from django.conf import settings
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from captcha.image import ImageCaptcha  # you need to `pip install captcha`
from redis.exceptions import ConnectionError


from .utils import verify_image_captcha





class GenerateImageCaptchaView(APIView):
    permission_classes = []

    def get(self, request):
        if not getattr(settings, "ENABLED_CAPTCHA", False):
            return Response({
                "captcha_id": "",
                "captcha_image": "",
                "message": "CAPTCHA is disabled."
            }, status=status.HTTP_200_OK)

        # Generate random 5-digit captcha text
        captcha_text = str(uuid.uuid4().int)[:5]
        captcha_id = str(uuid.uuid4())

        # Generate CAPTCHA image
        image = ImageCaptcha()
 

        image_data = image.generate(captcha_text)
        image_bytes = image_data.read()

        # Encode image as base64
        encoded_image = base64.b64encode(image_bytes).decode("utf-8")
        captcha_image_data = f"data:image/png;base64,{encoded_image}"

        try:
            # Save captcha answer in cache for 2 minutes
            cache.set(f"captcha:{captcha_id}", captcha_text, timeout=120)
        except ConnectionError:
            return Response({
                "error": "Service temporarily unavailable. Please try again later."
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return Response({
            "captcha_id": captcha_id,
            "captcha_image": captcha_image_data,
        }, status=status.HTTP_200_OK)




class VerifyImageCaptchaView(APIView):
    permission_classes = []

    def post(self, request):
        success, message = verify_image_captcha(request)

        if success:
            return Response({"success": True, "message": "CAPTCHA verified."}, status=status.HTTP_200_OK)
        else:
            return Response({"success": False, "error": message}, status=status.HTTP_400_BAD_REQUEST)



 