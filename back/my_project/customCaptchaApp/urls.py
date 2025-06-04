from django.urls import path
from .views import  GenerateImageCaptchaView, VerifyImageCaptchaView

urlpatterns = [
    # path("generate/", GenerateCaptchaView.as_view(), name="generate-captcha"),
    # path("validate/", ValidateCaptchaView.as_view(), name="validate-captcha"),


    path("generate_image_captcha/", GenerateImageCaptchaView.as_view() ),
    path("validate_image_captcha/", VerifyImageCaptchaView.as_view() ),

]
