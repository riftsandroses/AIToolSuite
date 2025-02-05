from django.shortcuts import render

def lab_option(request):
    return render(request, 'report/lab_option.html')

def ai_option(request):
    return render(request, 'report/ai_option.html')

def llm_scanner_report(request):
    return render(request, 'report/llm_scanner_report.html')