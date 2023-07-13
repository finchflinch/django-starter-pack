from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import get_user_model



# Create your views here.
@login_required
def home(request):
    context = {}
    return render(request, 'user/home.html', context)

def login(request):
    context = {}
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            # login success
            print('User exists')
            auth.login(request, user)
            return redirect(home)
        else:
            # dont say if user doesnt exist or exists. just throw blank errors
            print('incorrect email or password')
            return redirect(login)
    else:
        if request.user.is_authenticated:
            return redirect(home)
        else:
            return render(request, "user/login.html", context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect(login)
