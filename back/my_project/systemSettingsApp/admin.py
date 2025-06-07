from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import MainConfiguration
from django.contrib import admin
from .models import QueuedEmail


@admin.register(QueuedEmail)
class QueuedEmailAdmin(admin.ModelAdmin):
    list_display = ('to_email', 'subject', 'status', 'created_at', 'last_attempt')
    list_filter = ('status', 'created_at')
    search_fields = ('to_email', 'subject', 'last_error_message')
    readonly_fields = ('created_at', 'last_attempt', 'last_error_message', "last_error_message_date")



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