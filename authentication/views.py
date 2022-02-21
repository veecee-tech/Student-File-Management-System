from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm, UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from level_adviser.models import AdviserProfile
from student.forms import CreateStudent
from student.models import StudentProfile
from .models import Account


# Create your views here.


def user_login(request):

    forms = UserLoginForm()
    
    if request.user.is_authenticated and request.user.role==2:
        return redirect("adviser_home")
    if request.user.is_authenticated and request.user.role==3:
        return redirect("student_home")
    if request.user.is_authenticated and request.user.role==1:
        return redirect("login")

    if request.method == "POST":
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            
            if user:
                acct = Account.objects.get(username=username)
                acct.login_counter = acct.login_counter+1
                acct.save()
                login(request, user)
                if user.role == 2:
                    return redirect("adviser_home")
                elif user.role == 3:                
                        return redirect("student_home")   
                else:
                    # messages.error(request, "Access Denied")
                    return redirect("archive_home")
                
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect("login")

    context = {
        "forms": forms
    }
    return render(request, "authentication/login.html", context)


@login_required
def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def register_student(request):

    userprofile = AdviserProfile.objects.get(user_id = request.user.id)
    if not userprofile.first_name:
        return redirect("update-adviser")

    

    if request.method == 'POST':
        forms = UserCreationForm(request.POST)

        if forms.is_valid():
            forms.save()
            messages.success(request, "Student Created Successfully")
        # else:
        #     messages.error(request, "Could not validate credentials")
            return redirect("register")
    else:
        forms = UserCreationForm()
        
    context = {
        'forms': forms,
       
    }

    return render(request, 'adviser/register_student.html', context)

@login_required()
def change_password(request):
    
    

    if request.method =="POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password CHanged Succssfully")
            return redirect('change_password')

        else:
            messages.error(request, 'Please correct the error below.')
    
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form': form
    }

    return render(request, 'authentication/change_password.html', context)