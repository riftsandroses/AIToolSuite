from django.shortcuts import render

def report(request):
    return render(request, 'report/report.html')

def table(request):
    # This view will render the table.html page
    return render(request, 'report/table.html')
