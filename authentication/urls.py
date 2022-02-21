from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register-student/', views.register_student, name='register'),
    path('change-password/', views.change_password, name='change_password'),
]

