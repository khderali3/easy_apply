



from django.urls import path

from .views import MainConfigurationView, QueuedEmailView, QueuedEmailDeleteAllView, SiteSettingsView




urlpatterns = [
    path('staff/main_configuration/', MainConfigurationView.as_view()),
    path('staff/queued_email/', QueuedEmailView.as_view()),
    path('staff/queued_email/delete_all/', QueuedEmailDeleteAllView.as_view()),
    path("site/site_settings/", SiteSettingsView.as_view()),
]



