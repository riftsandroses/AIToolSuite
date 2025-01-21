from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class OpenAIIntegration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scan_name = models.CharField(max_length=255)
    description = models.TextField()
    model_name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    attack_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.attack_name}"

class AzureDeployment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scan_name = models.CharField(max_length=255)
    description = models.TextField()
    azure_model_name = models.CharField(max_length=255)
    azure_endpoint_url = models.URLField()
    azure_deployment_name = models.CharField(max_length=255)
    azure_api_key = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    attack_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.attack_name}"