from django.urls import path
from .views import *

urlpatterns = [
    path("dashboard/", student_dashboard, name="student_home"),
    path("update-profile/", update_student_profile_view, name="update-student"),
    path("upload/", upload_document_view, name="upload_doc"),
]
