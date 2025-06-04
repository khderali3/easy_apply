from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model

User = get_user_model()




class RequestService(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, db_index=True)
    speed = models.JSONField(null=True, blank=True)  
    custom_speed = models.CharField(max_length=10, blank=True, null=True)
    city= models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)  # Set once when created
    updated = models.DateTimeField(auto_now=True)      # Updated every time saved
    request_result_note = models.CharField(max_length=255, default='')

    created_ip_address = models.GenericIPAddressField(null=True, blank=True) 

    STATUS_OPTIONS = [
        ('received_request', 'received request'),
        ('replied_to_client', 'replied to client'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_OPTIONS, default='received_request')

    def __str__(self):
        return self.full_name    


    class Meta:
            ordering = ['-id']  



class RequestServicePrivateNote(models.Model):
    request_service = models.ForeignKey(RequestService, related_name="RequestServicePrivateNote_RequestService", on_delete=models.PROTECT,null=True, blank=True)
    user = models.ForeignKey(User, related_name="RequestServicePrivateNote_user", on_delete=models.PROTECT,null=True, blank=True)
    note = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)  # Set once when created
    updated = models.DateTimeField(auto_now=True) 
    created_ip_address = models.GenericIPAddressField(null=True, blank=True) 

    def __str__(self):
        return f"{self.user} - {self.note}"





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
    request_result_note = models.CharField(max_length=255, default='')
    created_ip_address = models.GenericIPAddressField(null=True, blank=True) 


    STATUS_OPTIONS = [
        ('received_request', 'received request'),
        ('replied_to_client ', 'replied to client '),
    ]
    status = models.CharField(max_length=50, choices=STATUS_OPTIONS, default='received_request')

    def __str__(self):
        return self.full_name 

    class Meta:
            ordering = ['-id']  

class RequestAgentPrivateNote(models.Model):
    request_agent = models.ForeignKey(RequestAgent, related_name="RequestAgentPrivateNote_request_agent", on_delete=models.PROTECT,null=True, blank=True)


    user = models.ForeignKey(User, related_name="RequestAgentNote_user", on_delete=models.PROTECT, null=True, blank=True)
    note = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)  # Set once when created
    updated = models.DateTimeField(auto_now=True) 
    created_ip_address = models.GenericIPAddressField(null=True, blank=True) 

    def __str__(self):
        return f"{self.user}"






class SpeedPackagePrice(models.Model):
    speed = models.CharField(max_length=20)
    speed_ar = models.CharField(max_length=20)
    traffic_limit = models.CharField(max_length=20 )
    traffic_limit_ar = models.CharField(max_length=20 )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.speed}"




class TrafficPackagePrice(models.Model):
    traffic = models.CharField(max_length=20 )
    traffic_ar = models.CharField(max_length=20 )

    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.traffic}"





class UnlimitedSpeedTrafficPackagePrice(models.Model):
    traffic = models.CharField(max_length=20 )
    traffic_ar = models.CharField(max_length=20 )

    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.traffic}"


