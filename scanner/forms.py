from django import forms
from .models import OpenAIIntegration

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
