# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

# Hardcoded role mapping for now — could extend later
USER_ROLES = {
    'admin@example.com': 'admin',
    'manager@example.com': 'manager',
    'guest@example.com': 'guest',
}

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')


def unauthorized_view(request):
    return render(request, 'accounts/unauthorized.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# from .models import UserProfile

from .models import AccessLog

@login_required
def dashboard_view(request):
    try:
        role = request.user.userprofile.role
    except UserProfile.DoesNotExist:
        role = 'guest'

    # Log this access
    AccessLog.objects.create(
        user=request.user,
        view_accessed=f"{role} dashboard"
    )

    if role == 'admin':
        return render(request, 'accounts/dashboard_admin.html')
    elif role == 'manager':
        return render(request, 'accounts/dashboard_manager.html')
    elif role == 'guest':
        return render(request, 'accounts/dashboard_guest.html')
    else:
        return redirect('unauthorized')

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def view_logs(request):
    logs = AccessLog.objects.all().order_by('-timestamp')
    return render(request, 'accounts/view_logs.html', {'logs': logs})
