from django.contrib import admin
from .models import Ship, Rule
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    # Hide first_name and last_name in edit view
    list_display = ('username', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups')}),
    )

    # Hide in add user form too
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ('id', 'ship_no', 'half', 'half_username', 'half_other', 'half_other_username', 'status', 'shipped_date')
    list_filter = ('status', 'shipped_date')
    search_fields = ('half', 'half_other', 'remarks', 'ship_no', 'half_username', 'half_other_username')

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ('article_number', 'rule_content')
    search_fields = ('article_number', 'rule_content')
    ordering = ('article_number',)
