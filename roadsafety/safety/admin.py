from django.contrib import admin
from .models import TrafficRule, TrafficSign, HazardReport, EmergencyContact, SafetyTip

@admin.register(TrafficRule)
class TrafficRuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category']

@admin.register(TrafficSign)
class TrafficSignAdmin(admin.ModelAdmin):
    list_display = ['name', 'sign_type', 'emoji']
    list_filter = ['sign_type']

@admin.register(HazardReport)
class HazardReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'hazard_type', 'location', 'status', 'reported_at', 'user']
    list_filter = ['status', 'hazard_type']
    list_editable = ['status']

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'description']

@admin.register(SafetyTip)
class SafetyTipAdmin(admin.ModelAdmin):
    list_display = ['tip', 'audience']
    list_filter = ['audience']
