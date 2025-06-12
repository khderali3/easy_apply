from django.contrib import admin
from django.apps import apps
from django.http import HttpResponseRedirect

 
from .models import AppIndexTitle, CardLabelRequestAgent, CardLabelRequestService, CardLabelCheckRequest, CardLabelServicePrices
 



solo_models = [AppIndexTitle, CardLabelRequestAgent, CardLabelRequestService, CardLabelCheckRequest, CardLabelServicePrices]

# Base admin class for singletons to prevent add/delete and redirect changelist to change page
class SingletonModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        config = self.model.get_solo()
        return HttpResponseRedirect(
            f"/admin/{self.model._meta.app_label}/{self.model._meta.model_name}/{config.pk}/change/"
        )





app_models = apps.get_app_config('easyApplyApp').get_models()

for model in app_models:
    if model not in solo_models:
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass

# Register singleton models with SingletonModelAdmin
for model in solo_models:
    try:
        admin.site.register(model, SingletonModelAdmin)
    except admin.sites.AlreadyRegistered:
        pass
