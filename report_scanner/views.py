from django.shortcuts import render
from scanner.models import OpenAIIntegration, AzureDeployment, ScanResult
from django.contrib.auth.decorators import login_required
import plotly.express as px
import json
from django.db.models import Count
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

    # Aggregate findings count by time (ignoring date)
    findings_over_time = (
        scan_results
        .values('created_at__time')  # Extract only the time part
        .annotate(count=Count('id'))
        .order_by('created_at__time')
    )

    # Convert query results into lists for Plotly
    times = [entry["created_at__time"].strftime("%H:%M:%S") for entry in findings_over_time]  # Format time as HH:MM:SS
    counts = [entry["count"] for entry in findings_over_time]

    # Create Plotly figure with dark mode
    fig = px.line(x=times, y=counts, labels={"x": "Time", "y": "No. of Findings"}, title="Findings Over Time")

    fig.update_layout(
        template="plotly_dark",  # Dark mode
        paper_bgcolor="#1e1e1e",  # Dark background
        plot_bgcolor="#1e1e1e",  # Dark grid background
        font=dict(color="white"),  # White text
    )

    fig.update_traces(mode="lines+markers", line=dict(color="blue"))  # Blue line for better visibility

    # Convert Plotly figure to JSON
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render(request, 'report_scanner/scanner_insights.html', {
        'scan_results': scan_results,
        'report_name': report_name,
        'graph_json': graph_json
    })