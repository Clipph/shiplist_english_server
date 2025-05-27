from django.contrib import admin
from .models import Ship, Rule

@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ('id', 'ship_no', 'half', 'half_username', 'half_other', 'half_other_username', 'status', 'shipped_date')
    list_filter = ('status', 'shipped_date')
    search_fields = ('half', 'half_other', 'remarks', 'ship_no', 'half_username', 'half_other_username')

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ('article_number', 'rule_content', 'rule_year')
    search_fields = ('article_number', 'rule_content', 'rule_year')
    ordering = ('article_number',)
