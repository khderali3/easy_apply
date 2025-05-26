from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model

User = get_user_model()




class RequestService(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, db_index=True)
    SPEED_OPTIONS = [
        ('3', '3'),
        ('5', '5'),
        ('10', '10'),
        ('15', '15'),
        ('custom', 'Custom speed'),

    ]

    speed = models.CharField(max_length=10, choices=SPEED_OPTIONS)
    custom_speed = models.CharField(max_length=10, blank=True, null=True)
    city= models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)  # Set once when created
    updated = models.DateTimeField(auto_now=True)      # Updated every time saved


    STATUS_OPTIONS = [
        ('received_request', 'received request'),
        ('replied_to_client ', 'replied to client '),
    ]
    status = models.CharField(max_length=50, choices=STATUS_OPTIONS)

    def __str__(self):
        return self.full_name    


class RequestServiceNote(models.Model):
    user = models.ForeignKey(User, related_name="RequestServiceNote_user", on_delete=models.PROTECT)
    note = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)  # Set once when created
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.user 




class RequestAgent(models.Model):

    AGENT_TYPE_OPTIONS = [
        ('sub_provider', 'sub_provider'),
        ('distributor ', 'distributor'),
        ('pos ', 'pos'),
    ]

    agent_type = models.CharField(max_length=50, choices=AGENT_TYPE_OPTIONS)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, db_index=True)
    city= models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)  # Set once when created
    updated = models.DateTimeField(auto_now=True)      # Updated every time saved


    STATUS_OPTIONS = [
        ('received_request', 'received request'),
        ('replied_to_client ', 'replied to client '),
    ]
    status = models.CharField(max_length=50, choices=STATUS_OPTIONS)

    def __str__(self):
        return self.full_name 



class RequestAgentNote(models.Model):
    user = models.ForeignKey(User, related_name="RequestAgentNote_user", on_delete=models.PROTECT)
    note = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)  # Set once when created
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.user 
