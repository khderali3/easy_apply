from celery import shared_task
from django.utils.html import strip_tags
from systemSettingsApp.models import MainConfiguration
import ssl
from django.utils.functional import cached_property 
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from .models import QueuedEmail
 


from django.core.mail.backends.smtp import EmailBackend  


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






from django.db import transaction


@shared_task(bind=True)
def send_email_task(self, email_id):

    config = MainConfiguration.get_solo()
    host = config.smtp_host.strip()
    # host = "test.test.test"
    log = None  # <--- Define it first

    try:
        log = QueuedEmail.objects.get(id=email_id)
    except:
        return
 
    if not log.can_send():
        return


    try:
 
        log.status = 'sending'
        log.save(update_fields=['status'])


        connection = CustomEmailBackend(
            host= host,
            
            port=config.smtp_port,
            username=config.smtp_host_user,
            password=config.smtp_host_user_password,
            use_tls=config.smtp_use_tls,
            use_ssl=config.smtp_use_ssl,
            fail_silently=False,
            timeout=15,
        )

        if log.is_html:
            plain_text_body = strip_tags(log.body)
            email = EmailMultiAlternatives(
                subject=log.subject,
                body=plain_text_body,
                from_email=config.smtp_host_user,
                to=[log.to_email],
                connection=connection,
            )
            email.attach_alternative(log.body, "text/html")
        else:
            email = EmailMultiAlternatives(
                subject=log.subject,
                body=log.body,
                from_email=config.smtp_host_user,
                to=[log.to_email],
                connection=connection,
            )

        email.send()
        log.status = 'sent'
        log.save(update_fields=['status'])


    except Exception as e:
        if log:
            log.status = 'failed'

            log.last_error_message = f" {host} -  {str(e)}"
            log.last_error_message_date = timezone.now()
            log.retries += 1

            log.save(update_fields=['status', 'last_error_message', 'last_error_message_date', 'retries' ])

 
 


 



@shared_task
def retry_failed_emails():
    # print('this retry_failed_emails is working ')
    failed_emails = QueuedEmail.objects.filter(status='failed')

    for email in failed_emails:
        if email.can_retry():
            send_email_task.delay(email.id)




