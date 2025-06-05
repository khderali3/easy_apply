from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
 


from django.utils import timezone
 
 
class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email=email,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(
            email,
            password=password,
            **kwargs
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    country = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255, default="")
    address = models.CharField(max_length=255, default="")
    phone_number = models.CharField(max_length=255, default="")
    email_notifications_enabled = models.BooleanField(default=False) 
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('ar', 'Arabic'),
        ]

    preferred_language = models.CharField(max_length=2,choices=LANGUAGE_CHOICES, default='en' )



    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name' ]

    def __str__(self):
        return self.email    

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


 

 
class CustomPermission(models.Model):
    class Meta:        
        managed = False   
        default_permissions = ()                                
        permissions = ( 
            ('user_managment', 'User Managment'),  

        )

