from django.urls import path
from . import views

urlpatterns = [
    path('UserCreation/', views.UserCreation, name='usercreation'),
    path('UserLogin/', views.UserLogin, name='userlogin'),
    path('Profile/', views.profile, name='profile'),
    path('About/', views.about, name='about'),
    path('UserLogout/', views.UserLogout, name='userlogout'),
    path('Change/', views.UserChangePassword, name='userchangepassword'),
    path('Set/', views.UserSetPassword, name='usersetpassword'),
    path('Navview/', views.NavView.as_view(), name='navview'),
]
