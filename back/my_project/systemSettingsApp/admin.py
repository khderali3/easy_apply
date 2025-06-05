from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import MainConfiguration


@admin.register(MainConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Prevent creation of multiple instances via admin
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def changelist_view(self, request, extra_context=None):
        # Automatically redirect to the singleton instance
        config = MainConfiguration.get_solo()
        return HttpResponseRedirect(f"/admin/{self.model._meta.app_label}/{self.model._meta.model_name}/{config.pk}/change/")