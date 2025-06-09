
from django.template import Template, Context
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

 
from systemSettingsApp.models import MainConfiguration
import validators

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.tokens import default_token_generator

from rest_framework.exceptions import ValidationError



from ..models import QueuedEmail

from ..tasks import send_email_task



from datetime import timedelta
from django.utils import timezone
 
 


# Use PasswordResetTokenGenerator explicitly
activation_token_generator = PasswordResetTokenGenerator()



def is_valid_smtp_host(value):
    return validators.domain(value) or validators.ipv4(value)
 





def is_valid_smtp_host(value):
    return validators.domain(value) or validators.ipv4(value)


def send_email(subject, body, to_email, is_html=False):
    """
    Validates configuration and queues the email for sending via Celery.
    """
    config = MainConfiguration.get_solo()

    if config.maintenance_mode:
        raise Exception("The system is currently in maintenance mode.")

    if not config.email_service_enabled:
        raise Exception("The Email Service is Disabled.")

    smtp_host = config.smtp_host.strip()
    if not is_valid_smtp_host(smtp_host):
        raise Exception("SMTP host address is not valid.")

    required_fields = [
        config.smtp_host,
        config.smtp_port,
        config.smtp_host_user,
        config.smtp_host_user_password,
    ]
    if not all(required_fields):
        raise Exception("Incomplete email configuration.")

    # If validation passes, delegate to Celery


    # Save email intent to DB
    queued = QueuedEmail.objects.create(
        subject=subject,
        body=body,
        to_email=to_email,
        is_html=is_html,
    )



    try:
        send_email_task.delay(queued.id)
    except Exception as e:
        raise Exception(f"Failed to queue email task: {str(e)}")





def send_activation_email(user, request):
    """
    Prepares and sends the activation email to the user using a language-specific template.
    Uses frontend_activation_url from MainConfiguration.
    """
    config = MainConfiguration.get_solo()

    # Encode UID and generate one-time token
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = activation_token_generator.make_token(user)

    # Construct frontend activation link
    activation_link = f"{config.frontend_activation_url}?uid={uid}&token={token}"

    # Select template based on default language
    language = config.default_language
    template_string = (
        config.activation_email_template_ar
        if language == "ar"
        else config.activation_email_template_en
    )



    if language == "ar":
        company_name = config.company_name_ar
        site_name = config.site_name_ar
    else :
        company_name = config.company_name
        site_name = config.site_name

 







    # Render the email body with context
    context = Context({
        'full_name': f"{user.first_name} {user.last_name}",
        'activation_link': activation_link,
        'company_name': company_name,
        'site_name': site_name,
    })
    template = Template(template_string)
    message_body = template.render(context)

    # Wrap in HTML with proper direction
    direction = "rtl" if language == "ar" else "ltr"
    html_message = f"""
    <html>
        <body style="direction: {direction}; text-align: { 'right' if direction == 'rtl' else 'left' }; font-family: sans-serif;">
            <pre style="white-space: pre-wrap;">{message_body}</pre>
        </body>
    </html>
    """

    # Email subject
    # subject = f"Activate your account on {config.site_name}"


    subjects = {
        "en": f"Activate your account on {site_name}",
        "ar": f"فعّل حسابك على {site_name}",
        # add other languages as needed
    }

    subject = subjects.get(language, subjects["en"])  # default to English if language not found





    # Send HTML email
    send_email(subject, html_message, user.email, is_html=True)












def send_reset_password_email(user, request):
    """
    Sends a reset password email if the user is allowed (based on time limit).
    """
    config = MainConfiguration.get_solo()
    now = timezone.now()

    # Check if cooldown has passed
    if user.last_password_reset_email_sent:
        elapsed = now - user.last_password_reset_email_sent
        wait_hours = config.reset_email_wait_hours
        if elapsed < timedelta(hours=wait_hours):
            remaining_minutes = int((timedelta(hours=wait_hours) - elapsed).total_seconds() // 60)
            raise ValidationError(
                f"Please wait {remaining_minutes} more minute(s) before requesting another password reset email."
            )

    # Generate token and uid
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    reset_link = f"{config.frontend_reset_password_url}?uid={uid}&token={token}"

    # Select language-specific template
    # language = config.default_language

    language = user.preferred_language

    template_string = (
        config.reset_password_template_ar
        if language == "ar"
        else config.reset_password_template_en
    )


    if language == "ar":
        company_name = config.company_name_ar
        site_name = config.site_name_ar
    else :
        company_name = config.company_name
        site_name = config.site_name

 


    # Render template with context
    context = Context({
        'full_name': f"{user.first_name} {user.last_name}",
        'reset_link': reset_link,
        'company_name': company_name,
        'site_name': site_name,
    })
    template = Template(template_string)
    message_body = template.render(context)

    # Wrap in HTML
    direction = "rtl" if language == "ar" else "ltr"
    html_message = f"""
    <html>
        <body style="direction: {direction}; text-align: {'right' if direction == 'rtl' else 'left'}; font-family: sans-serif;">
            <pre style="white-space: pre-wrap;">{message_body}</pre>
        </body>
    </html>
    """

    # Email subject

    # subject = f"Reset your password on {config.site_name}"

    subjects = {
        "en": f"Reset your password on {site_name}",
        "ar": f"إعادة تعيين كلمة المرور على {site_name}",
        # add other languages as needed
    }

    subject = subjects.get(language, subjects["en"])  # default to English if language not found


    # Send the email
    send_email(subject, html_message, user.email, is_html=True)

    # Update the last_password_reset_email_sent field
    user.last_password_reset_email_sent = now
    user.save(update_fields=['last_password_reset_email_sent'])
