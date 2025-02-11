from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def lab_option(request):
    return render(request, 'report/lab_option.html')

@login_required
def ai_option(request):
    return render(request, 'report/ai_option.html')
