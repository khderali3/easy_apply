# usersAuthApp/utils.py

from django.core.mail import EmailMultiAlternatives, get_connection
from django.template import Template, Context
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
 
from systemSettingsApp.models import MainConfiguration
import validators
 

 
 
 
from systemSettingsApp.models import MainConfiguration
import validators


import ssl
from django.core.mail.backends.smtp import EmailBackend  
from django.utils.functional import cached_property 


class CustomEmailBackend(EmailBackend):

    @cached_property
    def ssl_context(self):
        if self.ssl_certfile or self.ssl_keyfile:
            ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)
            ssl_context.load_cert_chain(self.ssl_certfile, self.ssl_keyfile)
            return ssl_context
        else:
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            return ssl_context




def is_valid_smtp_host(value):
    return validators.domain(value) or validators.ipv4(value)
 


# def send_email(subject: str, body: str, to_email: str):
#     """
#     Generic email sending function using SMTP settings from MainConfiguration.
#     """
#     config = MainConfiguration.get_solo()

#     if config.maintenance_mode:
#         raise Exception("The system is currently in maintenance mode.")

#     smtp_host = config.smtp_host.strip()
#     if not is_valid_smtp_host(smtp_host):
#         raise Exception("SMTP host address is not valid.")

#     required_fields = [
#         config.smtp_host,
#         config.smtp_port,
#         config.smtp_host_user,
#         config.smtp_host_user_password,
#     ]
#     if not all(required_fields):
#         raise Exception("Incomplete email configuration.")

#     if not is_valid_smtp_host(config.smtp_host):
#         raise Exception("SMTP Host Address no valied.")




#     try:
 
#         connection = CustomEmailBackend(
#             host=smtp_host,
#             port=config.smtp_port,
#             username=config.smtp_host_user,
#             password=config.smtp_host_user_password,
#             use_tls=config.smtp_use_tls,
#             use_ssl=config.smtp_use_ssl,
#             fail_silently=False
#         )



#         email = EmailMultiAlternatives(
#             subject=subject,
#             body=body,
#             from_email=config.smtp_host_user,
#             to=[to_email],
#             connection=connection,
#         )

#         email.send()

#     except Exception as e:
#         raise Exception(f"Failed to send email: {str(e)}")




# def send_activation_email(user, request):
#     """
#     Prepares and sends the activation email to the user using a language-specific template.
#     Uses frontend_activation_url from MainConfiguration.
#     """
#     config = MainConfiguration.get_solo()

#     # Encode UID and generate token
#     uid = urlsafe_base64_encode(force_bytes(user.pk))
#     token = default_token_generator.make_token(user)

#     # Construct frontend activation link
#     activation_link = f"{config.frontend_activation_url}?uid={uid}&token={token}"

#     # Choose email template based on default language
#     language = config.default_language
#     template_string = config.activation_email_template_ar if language == 'ar' else config.activation_email_template_en

#     # Render email message with template context
#     context = Context({
#         'full_name': f"{user.first_name} {user.last_name}",
#         'activation_link': activation_link,
#         'company_name': config.company_name,
#         'site_name': config.site_name,
#     })
#     template = Template(template_string)
#     message = template.render(context)

#     # Email subject and send
#     subject = f"Activate your account on {config.site_name}"
#     send_email(subject, message, user.email)





# def send_email(subject: str, body: str, to_email: str, is_html=False):
#     config = MainConfiguration.get_solo()

#     if config.maintenance_mode:
#         raise Exception("The system is currently in maintenance mode.")

#     smtp_host = config.smtp_host.strip()
#     if not is_valid_smtp_host(smtp_host):
#         raise Exception("SMTP host address is not valid.")

#     required_fields = [
#         config.smtp_host,
#         config.smtp_port,
#         config.smtp_host_user,
#         config.smtp_host_user_password,
#     ]
#     if not all(required_fields):
#         raise Exception("Incomplete email configuration.")

#     if not is_valid_smtp_host(config.smtp_host):
#         raise Exception("SMTP Host Address no valied.")




#     try:
#         connection = CustomEmailBackend(
#             host=config.smtp_host.strip(),
#             port=config.smtp_port,
#             username=config.smtp_host_user,
#             password=config.smtp_host_user_password,
#             use_tls=config.smtp_use_tls,
#             use_ssl=config.smtp_use_ssl,
#             fail_silently=False
#         )

#         email = EmailMultiAlternatives(
#             subject=subject,
#             body=body if not is_html else '',  # fallback text if needed
#             from_email=config.smtp_host_user,
#             to=[to_email],
#             connection=connection,
#         )

#         if is_html:
#             email.attach_alternative(body, "text/html")

#         email.send()

#     except Exception as e:
#         raise Exception(f"Failed to send email: {str(e)}")




from django.utils.html import strip_tags

def send_email(subject, body, to_email, is_html=False):
    config = MainConfiguration.get_solo()

    if config.maintenance_mode:
        raise Exception("The system is currently in maintenance mode.")

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

    try:
        connection = CustomEmailBackend(
            host=smtp_host,
            port=config.smtp_port,
            username=config.smtp_host_user,
            password=config.smtp_host_user_password,
            use_tls=config.smtp_use_tls,
            use_ssl=config.smtp_use_ssl,
            fail_silently=False
        )

        if is_html:
            plain_text_body = strip_tags(body)
            email = EmailMultiAlternatives(
                subject=subject,
                body=plain_text_body,  # fallback for non-HTML clients
                from_email=config.smtp_host_user,
                to=[to_email],
                connection=connection,
            )
            email.attach_alternative(body, "text/html")
        else:
            email = EmailMultiAlternatives(
                subject=subject,
                body=body,
                from_email=config.smtp_host_user,
                to=[to_email],
                connection=connection,
            )

        email.send()

    except Exception as e:
        raise Exception(f"Failed to send email: {str(e)}")




 
# def send_activation_email(user, request):
#     """
#     Prepares and sends the activation email to the user using a language-specific template.
#     Uses frontend_activation_url from MainConfiguration.
#     """
#     config = MainConfiguration.get_solo()

#     # Encode UID and generate token
#     uid = urlsafe_base64_encode(force_bytes(user.pk))
#     token = default_token_generator.make_token(user)


 
 

#     # Construct frontend activation link
#     activation_link = f"{config.frontend_activation_url}?uid={uid}&token={token}"

#     # Choose email template based on default language
#     language = config.default_language
#     template_string = config.activation_email_template_ar if language == 'ar' else config.activation_email_template_en

#     # Render email message with template context
#     context = Context({
#         'full_name': f"{user.first_name} {user.last_name}",
#         'activation_link': activation_link,
#         'company_name': config.company_name,
#         'site_name': config.site_name,
#     })
#     template = Template(template_string)
#     message_body = template.render(context)

#     # Wrap in HTML with direction based on language
#     direction = "rtl" if language == "ar" else "ltr"
#     html_message = f"""
#     <html>
#         <body style="direction: {direction}; text-align: { 'right' if direction == 'rtl' else 'left' };">
#             <pre style="font-family: inherit; white-space: pre-wrap;">{message_body}</pre>
#         </body>
#     </html>
#     """

#     # Email subject
#     subject = f"Activate your account on {config.site_name}"

#     # Send using HTML-capable method
#     send_email(subject, html_message, user.email, is_html=True)





from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template import Template, Context

# Use PasswordResetTokenGenerator explicitly
activation_token_generator = PasswordResetTokenGenerator()

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

    # Render the email body with context
    context = Context({
        'full_name': f"{user.first_name} {user.last_name}",
        'activation_link': activation_link,
        'company_name': config.company_name,
        'site_name': config.site_name,
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
    subject = f"Activate your account on {config.site_name}"

    # Send HTML email
    send_email(subject, html_message, user.email, is_html=True)
