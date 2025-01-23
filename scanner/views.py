from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OpenAIIntegrationForm, AzureDeploymentForm
from .models import OpenAIIntegration, AzureDeployment, ValueMapping
import os
import yaml
import uuid
from django.conf import settings
from django.shortcuts import render, redirect

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
        selected_attacks = request.POST.getlist('attacks')
        if selected_attacks:
            attack_names = ", ".join(selected_attacks)
            try:
                # Retrieve or create the latest OpenAIIntegration record
                integration = OpenAIIntegration.objects.filter(user=request.user).order_by('-created_at').first()
                if not integration:
                    integration = OpenAIIntegration.objects.create(
                        user=request.user,
                        scan_name="Default Scan Name"
                    )

                # Update the attack_name field
                integration.attack_name = attack_names

                # Generate probe_lists from selected attacks
                probe_names = []
                for attack in selected_attacks:
                    try:
                        value_mapping = ValueMapping.objects.get(attack_name=attack)
                        probe_names.append(value_mapping.probes_name)
                    except ValueMapping.DoesNotExist:
                        pass  # Skip if no mapping exists

                probe_lists_value = ",".join(probe_names)
                integration.probe_lists = probe_lists_value

                # Generate YAML
                yaml_file_name = f"{uuid.uuid4()}.yaml"
                yaml_file_path = os.path.join(settings.MEDIA_ROOT, yaml_file_name)

                yaml_data = {
                    'system': {
                        'verbose': 0,
                        'narrow_output': False,
                        'parallel_requests': False,
                        'parallel_attempts': False,
                        'lite': True,
                        'show_z': False,
                    },
                    'run': {
                        'seed': None,
                        'deprefix': True,
                        'eval_threshold': 0.5,
                        'generations': 5,
                        'probe_tags': None,
                    },
                    'plugins': {
                        'model_type': None,
                        'model_name': None,
                        'probe_spec': probe_lists_value,
                        'detector_spec': 'auto',
                        'extended_detectors': False,
                        'buff_spec': None,
                        'buffs_include_original_prompt': False,
                        'buff_max': None,
                        'detectors': {},
                        'generators': {},
                        'buffs': {},
                        'harnesses': {},
                        'probes': {
                            'encoding': {
                                'payloads': ['default']
                            }
                        },
                    },
                    'reporting': {
                        'report_prefix': None,
                        'taxonomy': None,
                        'report_dir': os.path.join(settings.MEDIA_URL),
                        'show_100_pass_modules': True,
                    },
                }

                # Save the YAML file
                os.makedirs(os.path.dirname(yaml_file_path), exist_ok=True)
                with open(yaml_file_path, 'w') as yaml_file:
                    yaml.dump(yaml_data, yaml_file, default_flow_style=False)

                # Save the YAML file name in the database
                integration.yaml_name = yaml_file_name
                integration.save()

                messages.success(request, f"YAML generated and saved: {yaml_file_name}")
            except Exception as e:
                messages.error(request, f"Error occurred: {str(e)}")
        else:
            messages.error(request, "No attacks were selected.")
        
        return redirect('scanner:homepage')

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
        selected_attacks = request.POST.getlist('attacks')
        if selected_attacks:
            attack_names = ", ".join(selected_attacks)
            try:
                # Retrieve or create the latest AzureDeployment record
                deployment = AzureDeployment.objects.filter(user=request.user).order_by('-created_at').first()
                if not deployment:
                    deployment = AzureDeployment.objects.create(
                        user=request.user,
                        scan_name="Default Deployment Name"
                    )

                # Update the attack_name field
                deployment.attack_name = attack_names

                # Generate probe_lists from selected attacks
                probe_names = []
                for attack in selected_attacks:
                    try:
                        value_mapping = ValueMapping.objects.get(attack_name=attack)
                        probe_names.append(value_mapping.probes_name)
                    except ValueMapping.DoesNotExist:
                        pass

                probe_lists_value = ",".join(probe_names)
                deployment.probe_lists = probe_lists_value

                # Generate YAML
                yaml_file_name = f"{uuid.uuid4()}.yaml"
                yaml_file_path = os.path.join(settings.MEDIA_ROOT, yaml_file_name)

                yaml_data = {
                    'system': {
                        'verbose': 0,
                        'narrow_output': False,
                        'parallel_requests': False,
                        'parallel_attempts': False,
                        'lite': True,
                        'show_z': False,
                    },
                    'run': {
                        'seed': None,
                        'deprefix': True,
                        'eval_threshold': 0.5,
                        'generations': 5,
                        'probe_tags': None,
                    },
                    'plugins': {
                        'model_type': None,
                        'model_name': None,
                        'probe_spec': probe_lists_value,
                        'detector_spec': 'auto',
                        'extended_detectors': False,
                        'buff_spec': None,
                        'buffs_include_original_prompt': False,
                        'buff_max': None,
                        'detectors': {},
                        'generators': {},
                        'buffs': {},
                        'harnesses': {},
                        'probes': {
                            'encoding': {
                                'payloads': ['default']
                            }
                        },
                    },
                    'reporting': {
                        'report_prefix': None,
                        'taxonomy': None,
                        'report_dir': os.path.join(settings.MEDIA_URL, 'garak_runs'),
                        'show_100_pass_modules': True,
                    },
                }

                # Save the YAML file
                os.makedirs(os.path.dirname(yaml_file_path), exist_ok=True)
                with open(yaml_file_path, 'w') as yaml_file:
                    yaml.dump(yaml_data, yaml_file, default_flow_style=False)

                # Save the YAML file name in the database
                deployment.yaml_name = yaml_file_name
                deployment.save()

                messages.success(request, f"YAML generated and saved: {yaml_file_name}")
            except Exception as e:
                messages.error(request, f"Error occurred: {str(e)}")
        else:
            messages.error(request, "No attacks were selected.")
        
        return redirect('scanner:homepage')

    return render(request, 'scanner/scanstarterazure.html', {'attack_options': attack_options})
