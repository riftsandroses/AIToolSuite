from django.contrib import admin
from .models import OpenAIIntegration

@admin.register(OpenAIIntegration)
class OpenAIIntegrationAdmin(admin.ModelAdmin):
    list_display = ['scan_name', 'user', 'created_at']
    search_fields = ['scan_name', 'user__username']
