from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model

User = get_user_model()




class AppSetting(models.Model):

    index_page_title =  models.CharField(max_length=255, blank=True, default="")
    index_page_title_ar =  models.CharField(max_length=255, blank=True, default="")
    max_request_user_service = models.PositiveIntegerField(default=10, help_text="Max requests allowed per user servic , if 0 no limits ")
    max_request_agent = models.PositiveIntegerField(default=10, help_text="Max requests allowed per agent, if 0 no limits")

    def __str__(self):
        return "App Settings"  
    
    @classmethod
    def get_solo(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj






 


class AppPricesTitle(models.Model):
    title =  models.CharField(max_length=255, blank=True, default="")
    title_ar =  models.CharField(max_length=255, blank=True, default="")
    title_hint =  models.CharField(max_length=255, blank=True, default="")
    title_hint_ar =  models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return self.title   
    
    @classmethod
    def get_solo(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj







class CardLabelRequestAgent(models.Model):
    title =  models.CharField(max_length=255, blank=True, default="")
    details = models.CharField(max_length=255, blank=True, default="")
    title_ar =  models.CharField(max_length=255, blank=True, default="")
    details_ar = models.CharField(max_length=255, blank=True, default="")
    bootstrap_icon = models.CharField(max_length=100, blank=True, default="bi-wifi")

    request_form_title = models.CharField(max_length=255, blank=True, default="")
    request_form_sub_title = models.CharField(max_length=255, blank=True, default="")
    request_form_title_ar = models.CharField(max_length=255, blank=True, default="")
    request_form_sub_title_ar = models.CharField(max_length=255, blank=True, default="")


    def __str__(self):
        return self.title    

    @classmethod
    def get_solo(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj



class CardLabelRequestService(models.Model):
    title =  models.CharField(max_length=255, blank=True, default="")
    details = models.CharField(max_length=255, blank=True, default="")
    title_ar =  models.CharField(max_length=255, blank=True, default="")
    details_ar = models.CharField(max_length=255, blank=True, default="")
    bootstrap_icon = models.CharField(max_length=100, blank=True, default="bi-wifi")

    request_form_title = models.CharField(max_length=255, blank=True, default="")
    request_form_sub_title = models.CharField(max_length=255, blank=True, default="")
    request_form_title_ar = models.CharField(max_length=255, blank=True, default="")
    request_form_sub_title_ar = models.CharField(max_length=255, blank=True, default="")





    def __str__(self):
        return self.title    

    @classmethod
    def get_solo(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    


class CardLabelCheckRequest(models.Model):
    title =  models.CharField(max_length=255, blank=True, default="")
    details = models.CharField(max_length=255, blank=True, default="")
    title_ar =  models.CharField(max_length=255, blank=True, default="")
    details_ar = models.CharField(max_length=255, blank=True, default="")
    bootstrap_icon = models.CharField(max_length=100, blank=True, default="bi-wifi")

    request_form_title = models.CharField(max_length=255, blank=True, default="")
    request_form_sub_title = models.CharField(max_length=255, blank=True, default="")
    request_form_title_ar = models.CharField(max_length=255, blank=True, default="")
    request_form_sub_title_ar = models.CharField(max_length=255, blank=True, default="")





    def __str__(self):
        return self.title    

    @classmethod
    def get_solo(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    

class CardLabelServicePrices(models.Model):
    title =  models.CharField(max_length=255, blank=True, default="")
    details = models.CharField(max_length=255, blank=True, default="")
    title_ar =  models.CharField(max_length=255, blank=True, default="")
    details_ar = models.CharField(max_length=255, blank=True, default="")
    bootstrap_icon = models.CharField(max_length=100, blank=True, default="bi-wifi")

    def __str__(self):
        return self.title    

    @classmethod
    def get_solo(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj







class RequestService(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, db_index=True)
    city= models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)  # Set once when created
    updated = models.DateTimeField(auto_now=True)      # Updated every time saved
    # request_result_note = models.CharField(max_length=255, default='')
    speed_package = models.JSONField(default=dict)
    created_ip_address = models.GenericIPAddressField(null=True, blank=True) 


    STATUS_OPTIONS = [
        ('pinding', 'Pinding'),
        ('complated', 'Complated'),
    ]

    status = models.CharField(max_length=50, choices=STATUS_OPTIONS, default='pinding')

    result_note  = models.CharField(max_length=255, blank=True, default="")

    type = models.CharField(default="service")

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
        ('distributor', 'distributor'),
        ('pos', 'pos'),
    ]


    BUSINESS_TYPE_OPTIONS = [
        ('shop', 'Shop'),
        ('company', 'Company'),
    ]
 
    business_type = models.CharField(max_length=50, choices=BUSINESS_TYPE_OPTIONS)
    agent_type = models.CharField(max_length=50, choices=AGENT_TYPE_OPTIONS)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, db_index=True)
    city= models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)  # Set once when created
    updated = models.DateTimeField(auto_now=True)      # Updated every time saved
    # request_result_note = models.CharField(max_length=255, default='')
    created_ip_address = models.GenericIPAddressField(null=True, blank=True) 


    STATUS_OPTIONS = [
        ('pinding', 'Pinding'),
        ('complated', 'Complated'),
    ]

    status = models.CharField(max_length=50, choices=STATUS_OPTIONS, default='pinding')
    result_note  = models.CharField(max_length=255, blank=True, default="")


    type = models.CharField(default="agent")

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





