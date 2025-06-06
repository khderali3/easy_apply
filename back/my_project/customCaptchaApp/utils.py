 
from django.conf import settings
from django.core.cache import cache
 
 
from redis.exceptions import ConnectionError

from systemSettingsApp.models import MainConfiguration


def verify_image_captcha(request):


    config = MainConfiguration.get_solo()

    if not getattr(config, "is_captcha_enabled", False):
        return True, ""

    captcha_id = request.data.get("captcha_id")
    user_input = request.data.get("captcha_input")

    if not captcha_id or not user_input:
        return False, "captcha_id and captcha_input are required."

    try:
        real_answer = cache.get(f"captcha:{captcha_id}")
    except ConnectionError:
        return False, "Service temporarily unavailable. Please try again later."

    if not real_answer:
        return False, "CAPTCHA expired or invalid."

    if str(real_answer).strip().lower() == str(user_input).strip().lower():
        try:
            cache.delete(f"captcha:{captcha_id}")
        except ConnectionError:
            pass
        return True, ""
    else:
        return False, "Incorrect CAPTCHA."

