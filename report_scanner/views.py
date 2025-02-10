from django.shortcuts import render
from scanner.models import OpenAIIntegration, AzureDeployment, ScanResult
from django.contrib.auth.decorators import login_required

@login_required
def report_list(request):
    openai_scans = OpenAIIntegration.objects.values('scan_name', 'created_at', 'description', 'model_name', 'yaml_name')
    azure_scans = AzureDeployment.objects.values('scan_name', 'created_at', 'description', 'azure_model_name', 'yaml_name')

    combined_scans = list(openai_scans) + list(azure_scans)

    return render(request, 'report_scanner/report_list.html', {'scans': combined_scans})


@login_required
def scanner_insights(request, yaml_name):
    # Remove .yaml extension
    base_name = yaml_name.replace('.yaml', '')

    # Query all rows in ScannerScanResult with report_name = base_name.hitlog.jsonl
    report_name = f"{base_name}.hitlog.jsonl"
    scan_results = ScanResult.objects.filter(report_name=report_name)

    return render(request, 'report_scanner/scanner_insights.html', {'scan_results': scan_results, 'report_name': report_name})