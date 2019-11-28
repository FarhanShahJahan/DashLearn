from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns=[
    path('', views.indexView, name="home"),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('login/',LoginView.as_view(), name= "login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', LogoutView.as_view(next_page='dashboard'), name="logout"),
    path('perf/', views.performView, name="performance"),
    path('profile/', views.profileView, name="profile"),
    path('profile/edit/', views.editprofileView, name="edit_profile"),
    path('assign/', views.assignmentView, name="assign"),
    path('course/', views.subjectView, name="subject")
]
 