from django.shortcuts import render
from student.models import StudentProfile, StudentDocuments
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def archive_home(request):

    return render(request, 'archive/archive_home.html')

@login_required
def search_archive(request):

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        if keyword:
            students = StudentProfile.objects.filter(adviser_id=None,mat_no__icontains=keyword)
        context = {
            'students': students
        }
    return render(request, 'archive/archive_home.html', context)
@login_required    
def alumni_document(request, pk):

   
        
    alumni_doc = StudentDocuments.objects.get(id = pk)

    context = {
        'alumni_doc': alumni_doc
    }

    return render(request,'archive/alumni_record.html',context)