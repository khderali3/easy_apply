from celery import shared_task
from django.utils.html import strip_tags
from systemSettingsApp.models import MainConfiguration
 

import ssl
from django.core.mail.backends.smtp import EmailBackend  
from django.utils.functional import cached_property 


from django.core.mail import EmailMultiAlternatives




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






@shared_task
def send_email_task(subject, body, to_email, is_html=False):
    try:
        config = MainConfiguration.get_solo()
        smtp_host = config.smtp_host.strip()

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
                body=plain_text_body,
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
        # You could log the error or retry depending on the configuration
        raise Exception(f"Failed to send email via Celery: {str(e)}")