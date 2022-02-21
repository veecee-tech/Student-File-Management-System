from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from authentication.models import Account

from django_currentuser.middleware import get_current_authenticated_user
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


@login_required
def student_dashboard(request):

    userprofile = StudentProfile.objects.get(user_id = request.user.id)
    if not userprofile.first_name:
        return redirect("update-student")
        
    return render(request, "student/dashboard.html")

@login_required 
def update_student_profile_view(request):
    
    
    forms = UpdateStudentProfileForm(instance=request.user.studentprofile)
    
    if request.method == "POST":
        forms = UpdateStudentProfileForm(request.POST, request.FILES or None, instance=request.user.studentprofile)

        if forms.is_valid():
            forms.save()
            messages.success(request, "Edit Student Info Successfully!")
            return redirect("update-student")

    context = {
        "forms": forms,
    }
    return render(request, "student/edit_student.html", context)

@login_required 
def upload_document_view(request):
    
    userprofile = StudentProfile.objects.get(user_id = request.user.id)
    if not userprofile.first_name:
        return redirect("update-student")

    if request.user.is_adviser:
        return redirect("adviser_home")
    if request.user.is_admin:
        return redirect("login")
    forms = ''
    if request.user.level == '100':
        
        if request.method == "POST":
            forms = UploadDocumentForm100(request.POST, request.FILES or None, instance=request.user.studentdocument)

            if forms.is_valid():
                forms.save()
                messages.success(request, "Upload Student Info Successfully!")
                return redirect("upload_doc")
        else:
            forms = UploadDocumentForm100(instance=request.user.studentdocument)
    
    if request.user.level == '200':
        
        if request.method == "POST":
            forms = UploadDocumentForm200(request.POST, request.FILES or None, instance=request.user.studentdocument)

            if forms.is_valid():
                forms.save()
                messages.success(request, "Upload Student Info Successfully!")
                return redirect("upload_doc")
        else:
            forms = UploadDocumentForm200(instance=request.user.studentdocument)
    
    if request.user.level == '300':
        
        if request.method == "POST":
            forms = UploadDocumentForm300(request.POST, request.FILES or None, instance=request.user.studentdocument)

            if forms.is_valid():
                forms.save()
                messages.success(request, "Upload Student Info Successfully!")
                return redirect("upload_doc")
        else:
            forms = UploadDocumentForm300(instance=request.user.studentdocument)

    if request.user.level == '400':
        
        if request.method == "POST":
            forms = UploadDocumentForm400(request.POST, request.FILES or None, instance=request.user.studentdocument)

            if forms.is_valid():
                forms.save()
                messages.success(request, "Upload Student Info Successfully!")
                return redirect("upload_doc")
        else:
            forms = UploadDocumentForm400(instance=request.user.studentdocument)
    
    if request.user.level == '500':
        
        if request.method == "POST" and userdoc.course_reg_500 is None:

            
            forms = UploadDocumentForm500(request.POST, request.FILES or None, instance=request.user.studentdocument)

            if forms.is_valid():
                forms.save()
                messages.success(request, "Upload Student Info Successfully!")
                return redirect("upload_doc")
        else:
            forms = UploadDocumentForm500(instance=request.user.studentdocument)
        

    context = {
        "forms": forms,
    }
    
    return render(request, "student/upload_doc.html", context)

