from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Try to find a user with the given email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
        
        if user and user.check_password(password):
            login(request, user)
            return redirect('/homepage/')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')

    return render(request, 'login/login.html')
