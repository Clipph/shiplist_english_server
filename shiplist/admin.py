from django.contrib import admin
from .models import Ship, Rule
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .admin_forms import ShipAdminForm
from django.db import models
from django import forms

admin.site.site_header = 'Shiplist Administration'

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

class CustomSplitDateTimeWidget(forms.SplitDateTimeWidget):
    def __init__(self, attrs=None):
        super().__init__(attrs=attrs)
        self.widgets = [
            forms.DateInput(attrs={'type': 'date'}),
            forms.TimeInput(attrs={'type': 'time'}),
        ]


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    form = ShipAdminForm

    formfield_overrides = {
        models.DateTimeField: {'widget': CustomSplitDateTimeWidget()},
    }

    list_display = ('ship_no', 'half', 'half_username', 'half_other', 'half_other_username', 'status', 'updated_by')
    list_editable = ('status',)
    list_display_links = ('ship_no', 'half', 'half_other')
    list_filter = ('status', 'shipped_date')
    search_fields = ('half', 'half_other', 'remarks', 'ship_no', 'half_username', 'half_other_username')
    exclude = ('updated_by',)

    # Dynamic read-only fields
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super().get_readonly_fields(request, obj))
        restricted_fields = ["half", "half_username", "half_other", "half_other_username"]

        if not request.user.has_perm("shiplist.can_edit_ship_entry"):
            readonly_fields.extend(restricted_fields)

        return readonly_fields

    # Security check to block tampering
    def save_model(self, request, obj, form, change):
        restricted_fields = {"half", "half_username", "half_other", "half_other_username"}
        if not request.user.has_perm("shiplist.can_edit_ship_entry"):
            if restricted_fields.intersection(form.changed_data):
                self.message_user(request, "You don't have permission to edit those fields.", level="error")
                return
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ('article_number', 'rule_content', 'updated_by')
    search_fields = ('article_number', 'rule_content')
    list_filter = ('section','updated_by',)
    search_fields = ('article_number', 'rule_content')
    ordering = ('article_number',)
    exclude = ('updated_by',)

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
