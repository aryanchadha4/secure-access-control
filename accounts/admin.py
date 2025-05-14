from django.contrib import admin
from .models import UserProfile, AccessLog

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role')
    list_filter = ('role',)

@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'view_accessed', 'timestamp')
    search_fields = ('user__username', 'view_accessed')
    list_filter = ('timestamp',)
