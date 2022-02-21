from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from authentication.models import Account
from student.models import StudentProfile, StudentDocuments

from django_currentuser.middleware import get_current_authenticated_user

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

@login_required
def adviser_dashboard(request):

    userprofile = AdviserProfile.objects.get(user_id = request.user.id)

    if not userprofile.first_name:
        return redirect("update-adviser")

    return render(request, "adviser/dashboard.html")


@login_required 
def update_adviser_profile_view(request):
    
    # if request.user.id != pk:
    #     return redirect("adviser_home")

    # user = Account.objects.get(id=pk)
    # adviser_edit = AdviserProfile.objects.get(user_id=pk)
    forms = UpdateAdviserProfileForm(instance=request.user.adviserprofile)
    
    if request.method == "POST":
        forms = UpdateAdviserProfileForm(request.POST, request.FILES or None, instance=request.user.adviserprofile)

        if forms.is_valid():
            forms.save()
            messages.success(request, "Edit adviser Info Successfully!")
            return redirect("update-adviser")

    context = {
        "forms": forms,
    }
    return render(request, "adviser/edit_adviser.html", context)


@login_required
def manage_students(request):

    userprofile = AdviserProfile.objects.get(user_id = request.user.id)
    if not userprofile.first_name:
        return redirect("update-adviser")

    students = StudentProfile.objects.filter(adviser_id = get_current_authenticated_user(),user__level=request.user.level)
    paginator = Paginator(students, 10)
    page = request.GET.get('page')
    paged_students = paginator.get_page(page)
    # product_count = products.count()
    context = {
        "students": paged_students
    }
    return render(request, "adviser/manage-students.html", context)

@login_required
def student_detail(request, pk):

    userprofile = AdviserProfile.objects.get(user_id = request.user.id)
    if not userprofile.first_name:
        return redirect("update-adviser")

    try:
        single_student = StudentProfile.objects.get(id=pk)
    except Exception as e:
        raise e
        
    if request.user.id != single_student.adviser.id:
        return redirect("adviser_home")


    context = {
        'single_student': single_student
    }
    return render(request, 'adviser/student_detail.html', context)

@login_required()
def delete_student(request, pk):

    userprofile = AdviserProfile.objects.get(user_id = request.user.id)
    if not userprofile.first_name:
        return redirect("update-adviser")

    try:
        single_student = StudentProfile.objects.get(id=pk)
        student = Account.objects.get(id=single_student.user.id)
    except Exception as e:
        raise e
        
    if request.user.id != single_student.adviser.id:
        return redirect("adviser_home")
    
    student.delete()
    messages.success(request, "Delete Student Info Successfully")
    return redirect("manage-students")

@login_required
def search_student(request):

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        if keyword:
            students = StudentProfile.objects.filter(adviser_id = get_current_authenticated_user(),first_name__icontains=keyword)
        context = {
            'students': students
        }
    return render(request, 'adviser/manage-students.html', context)

@login_required
def student_document(request, pk):

    userprofile = AdviserProfile.objects.get(user_id = request.user.id)
    if not userprofile.first_name:
        return redirect("update-adviser")
        
    student_doc = StudentDocuments.objects.get(id = pk)

    context = {
        'student_doc': student_doc
    }

    return render(request,'adviser/student_record.html',context)

@login_required
def update_students_level(request):

    students = StudentProfile.objects.filter(adviser_id = request.user.id)
    
    for i in students:
        user = Account.objects.get(id = i.user.id)
        user.level = request.user.level
        user.save()
    return redirect("manage-students")

@login_required
def move_to_archive(request, pk):

    student = StudentProfile.objects.get(user_id = pk, adviser_id = request.user.id)
    
    user = Account.objects.get(id = pk)
    user.level = 'ALUMNI'
    user.is_active = False
    user.save()

    student.adviser = None
    student.save()

    return redirect("manage-students")