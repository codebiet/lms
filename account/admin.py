from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import Account
from django.contrib.auth.models import Group

class AccountAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name','last_name', 'roll_no', 'branch', 'year')
    search_fields = ('email', 'first_name', 'last_name', 'roll_no')
    readonly_fields = ('id', 'date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = ()
    search_fields = ('email',)
    ordering = ('email',)
admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)
