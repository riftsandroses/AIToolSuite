from django.shortcuts import render
from scanner.models import OpenAIIntegration, AzureDeployment, ScanResult, ValueMapping
from django.contrib.auth.decorators import login_required
import plotly.express as px
import json
from django.db.models import Count, IntegerField
from django.db.models.functions import Cast
import plotly.utils

@login_required
def report_list(request):
    openai_scans = OpenAIIntegration.objects.values('scan_name', 'created_at', 'description', 'model_name', 'yaml_name')
    azure_scans = AzureDeployment.objects.values('scan_name', 'created_at', 'description', 'azure_model_name', 'yaml_name')

    combined_scans = list(openai_scans) + list(azure_scans)

    return render(request, 'report_scanner/report_list.html', {'scans': combined_scans})


@login_required
def scanner_insights(request, yaml_name):
    base_name = yaml_name.replace('.yaml', '')
    report_name = f"{base_name}.hitlog.jsonl"
    scan_results = ScanResult.objects.filter(report_name=report_name)

    # Define evaluation categories
    categories = [
        "Robustness Evaluation",
        "Adversarial Resilience",
        "Exploitation Resistance",
        "Ethical Alignment",
        "Hallucination Rate"
    ]

    category_status = {}

    for category in categories:
        # Get all ValueMappings for this category
        value_mappings = ValueMapping.objects.filter(category_matrix=category)
        
        # Collect all probes associated with this category
        category_probes = set()
        for mapping in value_mappings:
            category_probes.update(p.strip() for p in mapping.probes_name.split(','))

        # Check if there is a match in scan results
        matching_probes = scan_results.filter(probe__in=category_probes)

        if matching_probes.exists():
            category_status[category] = "Potential Issues Found"
        else:
            category_status[category] = "No Issues Found"

    # Generate graphs
    findings_over_time = (
        scan_results
        .values('created_at__time')  
        .annotate(count=Cast(Count('id'), IntegerField()))
        .order_by('created_at__time')
    )

    times = [entry["created_at__time"].strftime("%H:%M:%S") for entry in findings_over_time]  
    counts = [int(entry["count"]) for entry in findings_over_time]  

    fig = px.line(x=times, y=counts, labels={"x": "Time", "y": "No. of Findings"}, title="Findings Over Time")
    fig.update_layout(template="plotly_dark", paper_bgcolor="#1e1e1e", plot_bgcolor="#1e1e1e", font=dict(color="white"))
    fig.update_traces(mode="lines+markers", line=dict(color="blue"))  

    # Probe Analysis Pie Chart
    probe_counts = scan_results.values('probe').annotate(count=Cast(Count('id'), IntegerField()))

    probe_attack_mapping = {}
    all_mappings = ValueMapping.objects.values('probes_name', 'attack_name')

    for mapping in all_mappings:
        probes_list = [p.strip() for p in mapping["probes_name"].split(",")]  
        for probe in probes_list:
            probe_attack_mapping[probe] = mapping["attack_name"]

    data = []
    for entry in probe_counts:
        probe = entry["probe"]
        count = int(entry["count"])
        attack_name = probe_attack_mapping.get(probe, "Unknown")  
        data.append({"Attack Name": attack_name, "Count": count})

    if not data:
        fig2 = px.pie(title="No Data Available")
    else:
        fig2 = px.pie(
            names=[entry["Attack Name"] for entry in data],
            values=[entry["Count"] for entry in data],
            title="Attack Name Distribution",
            hole=0.4
        )

        fig2.update_layout(
            template="plotly_dark",
            paper_bgcolor="#1e1e1e",
            plot_bgcolor="#1e1e1e",
            font=dict(color="white")
        )

        fig2.update_traces(textinfo="label+percent")

    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graph_json2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    return render(request, 'report_scanner/scanner_insights.html', {
        'scan_results': scan_results,
        'report_name': report_name,
        'category_status': category_status,
        'graph_json': graph_json,
        'graph_json2': graph_json2
    })
