from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from .models import Profile


class ProfileInline(admin.StackedInline):
    """Inline user profile in user admin"""
    model = Profile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username', 'email', 'get_phone_number', 'first_name', 'last_name',
        'is_staff')
    list_select_related = ('profile',)

    def get_phone_number(self, instance):
        return instance.profile.phone_number

    get_phone_number.short_description = _('phone number')

    def get_inline_instances(self, request, obj=None):
        """When creating a new user don't show profile one the first step"""
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
