from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html


class AccountAdmin(UserAdmin):
    """
    Customizes the display of admin user fields
    It displayes the date joined and last login fields as readonly
    and also leaves the password field as readonly
    """
    list_display = ('first_name', 'last_name', 'username',
                    'email', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UserProfileAdmin(admin.ModelAdmin):
    # Customizes the display of user profiles
    def thumbnail(self, object):
        # User profile image thumbnail
        return format_html('<img src="{}" width="50" height="50" style="border-radius:50%;">'.format(object.profile_picture.url))

    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'country', 'state', 'city')


admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
