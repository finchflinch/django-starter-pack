from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import get_user_model

from flow.models import Flow, FlowName
from form.models import SalesToVendor
from .models import Role


# Create your views here.
@login_required
def home(request):
    context = {}
    user = request.user
    if user.role.role_name in ['PLANNING', 'PLANT STORE', 'PLANT HEAD', 'FINANCE']:
        flow_type = FlowName(flow_name = 'Sales To Vendor')
        pending_at_role = Role(role_name=user.role.role_name)
        print(pending_at_role)
        flow= Flow(pending_at_role=pending_at_role)
        print(flow)
        pending_requests = SalesToVendor.objects.filter(status='IN_PROCESS', company_code=user.company, reach_code__pending_at_role__role_name=user.role)
        print(pending_requests)
        context["pending_requests"] = pending_requests


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
