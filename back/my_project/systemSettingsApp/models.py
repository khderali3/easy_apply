from django.db import models

# Create your models here.



from django.core.exceptions import ValidationError
from PIL import Image
import os
from io import BytesIO
from django.core.files.base import ContentFile


def validate_logo(value):
    if not value.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        raise ValidationError("Only image files (.png, .jpg, .jpeg, .gif) are allowed.")






class MainConfiguration(models.Model):
    # Singleton pattern (only one row allowed)
    company_name = models.CharField(max_length=255,default="My Company")
    company_name_ar = models.CharField(max_length=255,default="إسم الشركة")

    site_name = models.CharField(max_length=255,default="My Site Name")
    site_name_ar = models.CharField(max_length=255,default="اسم الموقع")


    frontend_activation_url = models.URLField(
        default="http://localhost:3000/account/activate-account",  # or your production default
        help_text="Base frontend URL for account activation, e.g. http://example.com/activate-account"
    )





    frontend_reset_password_url = models.URLField(
        default="http://localhost:3000/account/reset_password",   
        help_text="Base frontend URL for reset_password, e.g. http://example.com/reset_password"
    )



    support_email = models.EmailField(default="supprt@test.local")
    company_logo = models.ImageField(upload_to="company_logo/", null=True, blank=True, validators=[validate_logo])
 
    phone_number = models.CharField(max_length=50,default="000000000")
    fax_number = models.CharField(max_length=50, default="000000000")


    address = models.TextField(default="test1-test2")
    address_ar = models.TextField(default="test1-test2")



    # Email Templates (can be TextField or use a related model if multi-template)
    reset_password_template_en = models.TextField(default="""
        Hello {{ full_name }},

        We received a request to reset your password for your {{ site_name }} account.

        To reset your password, click the link below:

        {{ reset_link }}

        If you didn’t request a password reset, you can ignore this email. Your password will remain unchanged.

        Thank you,  
        The {{ company_name }} Team
        """)


    reset_password_template_ar = models.TextField(default="""
        مرحبًا {{ full_name }},

        لقد تلقينا طلبًا لإعادة تعيين كلمة المرور لحسابك في {{ site_name }}.

        لإعادة تعيين كلمة المرور الخاصة بك، يرجى الضغط على الرابط أدناه:

        {{ reset_link }}

        إذا لم تطلب إعادة تعيين كلمة المرور، يمكنك تجاهل هذه الرسالة. ستبقى كلمة المرور الخاصة بك دون تغيير.

        شكرًا لك،  
        فريق {{ company_name }}
        """)
    
    # activation_email_template_en = models.TextField( default="test1-test2")

    activation_email_template_en = models.TextField(default="""
        Hello {{full_name}},

        Thank you for registering at {{site_name}}!

        Please click the link below to activate your account:

        {{activation_link}}

        If you did not sign up for this account, please ignore this email.

        Best regards,  
        {{company_name}} Team
        """)

    activation_email_template_ar = models.TextField(default="""
        مرحبًا {{full_name}}،

        شكرًا لتسجيلك في {{site_name}}!

        يرجى النقر على الرابط أدناه لتفعيل حسابك:

        {{activation_link}}

        إذا لم تقم بإنشاء هذا الحساب، يمكنك تجاهل هذه الرسالة.

        مع تحيات،  
        فريق {{company_name}}
        """)



    reset_email_wait_hours = models.PositiveIntegerField(
        default=1,
        help_text="Minimum number of hours required between password reset emails for the same user."
    )




    # Email settings

    email_service_enabled = models.BooleanField(default=True)

    allow_registration_without_email_verification = models.BooleanField(default=False)


    smtp_host = models.CharField(max_length=255,  default="smtp.test.local")
    smtp_port = models.PositiveIntegerField( default=465)
    smtp_host_user = models.EmailField( default="user@test.local")
    smtp_host_user_password = models.CharField(max_length=255,   default="00000000")
    smtp_use_tls = models.BooleanField(default=False)
    smtp_use_ssl = models.BooleanField(default=False)

    # Localization / Language options
    default_language = models.CharField(max_length=2, choices=[('en', 'English'), ('ar', 'Arabic')], default='en')

 

    is_captcha_enabled =models.BooleanField(default=True)

    # Control flags
    maintenance_mode = models.BooleanField(default=False)
    allow_user_registration = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "main Configuration"
        verbose_name_plural = "main Configuration"

    def __str__(self):
        return "main Configuration"

 

    def save(self, *args, **kwargs):
        # Enforce singleton pattern
        self.pk = 1
        super().save(*args, **kwargs)

        # Resize image if needed
        if self.company_logo:
            logo_path = self.company_logo.path
            try:
                img = Image.open(logo_path)
                max_size = (500, 500)
                if img.height > 500 or img.width > 500:
                    img.thumbnail(max_size, Image.ANTIALIAS)
                    img.save(logo_path)
            except Exception as e:
                # Optional: Log the error if needed
                pass
 
 

    @classmethod
    def get_solo(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

