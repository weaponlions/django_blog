from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.views.generic.base import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

# Create your views here.

def UserCreation(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = UserCreationForm(request.POST)
            if fm.is_valid():
                fm.save()
                return redirect('/app3/UserLogin')
            else:
                return render(request, 'app3/form.html', {'form': fm, 'action' : 'usercreation', 'button' : 'Sign_Up', 'heading' : 'User Create Form', 'title': 'USER SIGNUP FORM'})
        else:
            return render(request, 'app3/form.html', {'form': UserCreationForm(), 'action' : 'usercreation', 'button' : 'Sign_Up', 'heading' : 'User Create Form', 'title': 'USER SIGNUP FORM'})
    else:
        return redirect('/app3/Profile')


def UserLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                user = authenticate(username=fm.cleaned_data['username'], password=fm.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('/app3/Profile')
                else:
                    return render(request, 'app3/form.html', {'form': fm, 'action' : 'userlogin', 'button' : 'Sign_In', 'heading' : 'User Login Form', 'title': 'USER LOGIN FORM'})
            else:
                return render(request, 'app3/form.html', {'form': fm, 'action' : 'userlogin', 'button' : 'Sign_In', 'heading' : 'User Login Form', 'title': 'USER LOGIN FORM'})
        else:
            return render(request, 'app3/form.html', {'form': AuthenticationForm(), 'action' : 'userlogin', 'button' : 'Sign_In', 'heading' : 'User Login Form', 'title': 'USER LOGIN FORM'})
    else:
        return redirect('/app3/Profile')

@login_required(login_url='/app3/UserLogin')
def profile(request):
    return render(request, 'app3/profile.html', {'heading': 'Welcome to Profile Page User - @{}'.format(request.user), 'title': 'USER DASHBOARD'})

@staff_member_required(login_url='/app3/UserLogin')
def about(request):
    return render(request, 'app3/profile.html', {'heading': 'Welcome to About Page User - @{}'.format(request.user), 'title': 'ABOUT US'})


def UserLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/app3/UserLogin')
    else: 
        return redirect('/app3/UserLogin')

class NavView(TemplateView):
    template_name = "app3/temp.html"




def UserSetPassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return redirect('/app3/Profile')
            else:
                return render(request, 'app3/form.html', {'form': fm, 'action' : 'usersetpassword', 'button' : 'Set Password', 'heading' : 'User SET Password Form', 'title': 'SET PASSWORD FORM'})
        else:
            return render(request, 'app3/form.html', {'form': SetPasswordForm(user=request.user), 'action' : 'usersetpassword', 'button' : 'Set Password', 'heading' : 'User SET Password Form', 'title': 'SET PASSWORD FORM'})
    else:
        return redirect('/app3/UserLogin')


def UserChangePassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                return redirect('/app3/Profile')
            else:
                return render(request, 'app3/form.html', {'form': fm, 'action' : 'userchangepassword', 'button' : 'Change Password', 'heading' : 'User Change Password Form', 'title': 'CHANGE PASSWORD FORM'})
        else:
            return render(request, 'app3/form.html', {'form': PasswordChangeForm(user=request.user), 'action' : 'userchangepassword', 'button' : 'Change Password', 'heading' : 'User Change Password Form', 'title': 'CHANGE PASSWORD FORM'})
    else:
        return redirect('/app3/UserLogin')
