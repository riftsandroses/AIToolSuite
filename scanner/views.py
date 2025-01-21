from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OpenAIIntegrationForm

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
            return redirect('scanner:homepage')
    else:
        form = OpenAIIntegrationForm()

    return render(request, 'scanner/openai.html', {'form': form})
