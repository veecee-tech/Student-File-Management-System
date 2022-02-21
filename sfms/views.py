from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.views import user_login

def index(request):
    if request.user.is_authenticated and request.user.role==2:
        return redirect("adviser_home")
    if request.user.is_authenticated and request.user.role==3:
        return redirect("student_home")
    if request.user.is_authenticated and request.user.role==1:
        return redirect("archive_home")
        
    return redirect("login")
