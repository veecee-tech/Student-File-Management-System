from django.urls import path, include
from .views import *


urlpatterns = [
    
    path("dashboard/", adviser_dashboard, name="adviser_home"),
    path("manage-students/", manage_students, name="manage-students"),
    path("update-profile/", update_adviser_profile_view, name="update-adviser"),
    path("student-detail/<int:pk>", student_detail, name="student-detail"),
    path("student-docs/<int:pk>", student_document, name="student-document"),
    path('student/delete/<int:pk>', delete_student, name='delete_student'),
    path('search/', search_student, name="search"),
    path('update-level/', update_students_level, name='update-level'),
    path('archive/<int:pk>', move_to_archive, name='move_to_alumni'),

]
