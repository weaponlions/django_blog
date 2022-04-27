from django.urls import path
from . import views
from django.contrib.auth import views as auths

urlpatterns = [
    path('dashboard/', views.TemplateView.as_view(template_name='custom/dashboard.html'), name='dashboard'),
    path('login/', auths.LoginView.as_view(template_name='custom/login.html'), name='login'),
    path('logout/', auths.LogoutView.as_view(template_name='custom/logout.html'), name='logout'),
    path('change/', auths.PasswordChangeView.as_view(template_name='custom/password.html', success_url='/password_reset/done'), name='passwordchange'),
    path('change/done', auths.PasswordChangeDoneView.as_view(template_name='custom/done.html'), name='passwordchangedone'),
    path('reset/', auths.PasswordResetView.as_view(template_name='custom/password.html', success_url='/password_reset/done'), name='passwordreset'),
    path('reset/done', auths.PasswordResetDoneView.as_view(template_name='custom/done.html'), name='passwordresetdone'),
]
