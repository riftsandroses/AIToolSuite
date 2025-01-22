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

            try:
                # Retrieve the latest OpenAIIntegration for the user
                integration = OpenAIIntegration.objects.filter(user=request.user).order_by('-created_at').first()  # Get the latest record

                if not integration:
                    # If no integration exists, create a new one
                    integration = OpenAIIntegration.objects.create(
                        user=request.user,
                        scan_name="Default Scan Name"  # Provide default values if needed
                    )

                # Update the attack_name field
                integration.attack_name = attack_names

                # Now, process the attack names to get corresponding probes
                probe_names = []
                attack_list = attack_names.split(", ")  # Split the string by commas

                for attack in attack_list:
                    try:
                        value_mapping = ValueMapping.objects.get(attack_name=attack)
                        probe_names.append(value_mapping.probes_name)
                    except ValueMapping.DoesNotExist:
                        pass  # If the attack doesn't have a corresponding probes_name, skip it

                # Join all the probes names with commas and save them in the probe_lists column
                integration.probe_lists = ",".join(probe_names)
                integration.save()

                messages.success(request, "Attacks saved: " + attack_names)
            except Exception as e:
                messages.error(request, f"Error occurred: {str(e)}")

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

            try:
                # Retrieve the latest AzureDeployment for the user
                deployment = AzureDeployment.objects.filter(user=request.user).order_by('-created_at').first()  # Get the latest record

                if not deployment:
                    # If no deployment exists, create a new one
                    deployment = AzureDeployment.objects.create(
                        user=request.user,
                        scan_name="Default Deployment Name"  # Provide default values if needed
                    )

                # Update the attack_name field
                deployment.attack_name = attack_names

                # Now, process the attack names to get corresponding probes
                probe_names = []
                attack_list = attack_names.split(", ")  # Split the string by commas

                for attack in attack_list:
                    try:
                        value_mapping = ValueMapping.objects.get(attack_name=attack)
                        probe_names.append(value_mapping.probes_name)
                    except ValueMapping.DoesNotExist:
                        pass  # If the attack doesn't have a corresponding probes_name, skip it

                # Join all the probes names with commas and save them in the probe_lists column
                deployment.probe_lists = ",".join(probe_names)
                deployment.save()

                messages.success(request, "Attacks saved: " + attack_names)
            except Exception as e:
                messages.error(request, f"Error occurred: {str(e)}")

        else:
            messages.error(request, "No attacks were selected.")
        
        return redirect('scanner:homepage')  # Redirect to the homepage or another page

    return render(request, 'scanner/scanstarterazure.html', {'attack_options': attack_options})
