from django.contrib import admin
from usersAuthApp.models import UserAccount 
# Register your models here.
from django.contrib.auth.admin import UserAdmin


 



class EmployeeAdmin(UserAdmin):
#    ordering = ('email',)
#    list_display = ['email']
    list_display = ("email", "first_name", "last_name", "is_staff", "is_email_verified", "last_password_reset_email_sent", "preferred_language" )
    search_fields = ("email", "first_name", "last_name")
    list_filter = ('is_staff', 'is_superuser', "last_password_reset_email_sent")
    ordering = ("email",)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "is_email_verified",
                    "last_password_reset_email_sent",
                    "preferred_language"
  
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )


admin.site.register( UserAccount , EmployeeAdmin)



 