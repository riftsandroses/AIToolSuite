from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OpenAIIntegrationForm, AzureDeploymentForm
from .models import OpenAIIntegration, AzureDeployment, ValueMapping

@login_required
def homepage(request):
    return render(request, 'scanner/homepage.html')

@login_required
def openai_integration(request):
    if request.method == 'POST':
        form = OpenAIIntegrationForm(request.POST)
        if form.is_valid():
            integration = form.save(commit=False)
            integration.user = request.user
            integration.save()
            messages.success(request, "Data saved successfully!")
            return redirect('scanner:scanstarter_openai')
    else:
        form = OpenAIIntegrationForm()

    return render(request, 'scanner/openai.html', {'form': form})

@login_required
def azure_deployment(request):
    if request.method == 'POST':
        form = AzureDeploymentForm(request.POST)
        if form.is_valid():
            deployment = form.save(commit=False)
            deployment.user = request.user
            deployment.save()
            messages.success(request, "Azure Deployment data saved successfully!")
            return redirect('scanner:scanstarter_azure')
    else:
        form = AzureDeploymentForm()

    return render(request, 'scanner/azure.html', {'form': form})

@login_required
def scanstarter_openai(request):
    attack_options = [
        "Attack Generation Test",
        "Anti-Virus Spam Attacks",
        "Continuation Attacks",
        "Jailbreak Attacks",
        "Divergence Attacks",
        "Do Not Answer Bypass",
        "Encoding Injection",
        "File Format Attacks",
        "Glitch Attacks",
        "Goodside Attacks",
        "Skewed Identity Attacks",
        "Latent Injection Attack",
        "Language Model Risk Card (LMRC) Attacks",
        "Malware Generation Test",
        "False Assertion Attack",
        "Package Hallucination Attacks",
        "Prompt Injection Attacks",
        "Real Toxicity Attack",
        "Snowball Attack",
        "Suffix Attack",
        "TAP Attack",
        "Topic Attack",
        "Altered XSS Attack",
    ]

    if request.method == 'POST':
        selected_attacks = request.POST.getlist('attacks')  # Get the list of selected attacks
        if selected_attacks:
            attack_names = ", ".join(selected_attacks)  # Convert the list to a comma-separated string
            
            # Fetch the existing integration for the user
            integration, created = OpenAIIntegration.objects.get_or_create(
                user=request.user,
                defaults={
                    'scan_name': "Default Scan Name"  # Provide default values if needed
                }
            )
            
            # Update the attack_name field
            integration.attack_name = attack_names
            integration.save()

            messages.success(request, "Attacks saved: " + attack_names)
        else:
            messages.error(request, "No attacks were selected.")
        
        return redirect('scanner:homepage')  # Redirect to the homepage or another page

    return render(request, 'scanner/scanstarteropenai.html', {'attack_options': attack_options})

@login_required
def scanstarter_azure(request):
    attack_options = [
        "Attack Generation Test",
        "Anti-Virus Spam Attacks",
        "Continuation Attacks",
        "Jailbreak Attacks",
        "Divergence Attacks",
        "Do Not Answer Bypass",
        "Encoding Injection",
        "File Format Attacks",
        "Glitch Attacks",
        "Goodside Attacks",
        "Skewed Identity Attacks",
        "Latent Injection Attack",
        "Language Model Risk Card (LMRC) Attacks",
        "Malware Generation Test",
        "False Assertion Attack",
        "Package Hallucination Attacks",
        "Prompt Injection Attacks",
        "Real Toxicity Attack",
        "Snowball Attack",
        "Suffix Attack",
        "TAP Attack",
        "Topic Attack",
        "Altered XSS Attack",
    ]

    if request.method == 'POST':
        selected_attacks = request.POST.getlist('attacks')  # Get the list of selected attacks
        if selected_attacks:
            attack_names = ", ".join(selected_attacks)  # Convert the list to a comma-separated string

            # Fetch the existing deployment for the user
            deployment, created = AzureDeployment.objects.get_or_create(
                user=request.user,
                defaults={
                    'deployment_name': "Default Deployment Name"  # Provide default values if needed
                }
            )

            # Update the attack_name field
            deployment.attack_name = attack_names
            deployment.save()

            messages.success(request, "Attacks saved: " + attack_names)
        else:
            messages.error(request, "No attacks were selected.")
        
        return redirect('scanner:homepage')  # Redirect to the homepage or another page

    return render(request, 'scanner/scanstarterazure.html', {'attack_options': attack_options})