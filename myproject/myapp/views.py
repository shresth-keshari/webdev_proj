from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LoginData

def login_page(request):
    """Render the login page."""
    return render(request, 'login.html')

def submit_login(request):
    """Handle login form submission and save data to the database."""
    if request.method == 'POST':
        username = request.POST.get('username')  # Get the username
        password = request.POST.get('password')  # Get the password

        # Save the data to the database
        LoginData.objects.create(username=username, password=password)

        # Simple success response
        return HttpResponse("Your login data has been submitted and saved!")
    return redirect('login_page')  # Redirect if the method is not POST
