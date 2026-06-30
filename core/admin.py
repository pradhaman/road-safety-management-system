from django.contrib import admin
from .models import Profile, TrafficRule, TrafficSign, SafetyTip, EmergencyContact, HazardReport


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone_number', 'city', 'created_at')
    list_filter = ('role',)
    search_fields = ('user__username', 'phone_number', 'city')


@admin.register(TrafficRule)
class TrafficRuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'penalty')
    search_fields = ('title', 'description')


@admin.register(TrafficSign)
class TrafficSignAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(SafetyTip)
class SafetyTipAdmin(admin.ModelAdmin):
    list_display = ('title', 'audience', 'created_at')
    list_filter = ('audience',)
    search_fields = ('title', 'content')


@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'phone_number', 'region')
    list_filter = ('category',)
    search_fields = ('name', 'phone_number', 'region')


@admin.register(HazardReport)
class HazardReportAdmin(admin.ModelAdmin):
    list_display = ('hazard_type', 'location', 'severity', 'status', 'reported_by', 'reported_at')
    list_filter = ('status', 'severity', 'hazard_type')
    search_fields = ('location', 'description', 'reported_by__username')
    list_editable = ('status',)
    date_hierarchy = 'reported_at'
