from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from scanner import views

@login_required
def tres(request):
    return render(request, 'tres/homepage.html')

@login_required
def llmtool(request):
    return render(request, 'tres/llmtool.html')