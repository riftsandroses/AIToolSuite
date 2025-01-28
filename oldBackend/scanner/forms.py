from django import forms
from .models import OpenAIIntegration
from .models import AzureDeployment

class OpenAIIntegrationForm(forms.ModelForm):
    class Meta:
        model = OpenAIIntegration
        fields = ['scan_name', 'description', 'model_name', 'api_key']
        widgets = {
            'scan_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Scan Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}),
            'model_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Model Name'}),
            'api_key': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter OpenAI API Key'}),
        }

class AzureDeploymentForm(forms.ModelForm):
    class Meta:
        model = AzureDeployment
        fields = [
            'scan_name', 'description', 'azure_model_name', 
            'azure_endpoint_url', 'azure_deployment_name', 'azure_api_key'
        ]
        widgets = {
            'scan_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Scan Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}),
            'azure_model_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Azure Model Name'}),
            'azure_endpoint_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Azure Endpoint URL'}),
            'azure_deployment_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Azure Deployment Name'}),
            'azure_api_key': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Azure API Key'}),
        }