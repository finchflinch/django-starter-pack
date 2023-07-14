from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import SalesToVendorForm
from .models import SalesToVendor
from flow.models import FlowName, Flow

# Create your views here.
@login_required
def sales_to_vendor_form(request):
    flow_name_value = "Sales To Vendor"
    context = {}
    if request.method == 'POST':
        form = SalesToVendorForm(request.POST, user=request.user)
        if form.is_valid():
            form.fields['status'] = 'IN_PROCESS'
            # get salesToVendor object
            flow_type = FlowName.objects.get(flow_name=flow_name_value)
            reach_code = Flow.objects.get(flow_name=flow_type, reach_code=1)
            # form.fields['reach_code'].initial = reach_code
            form.instance.reach_code = reach_code
            # print(form.fields['reach_code'])
            form.save()
            context['msg'] = 'form saved successfully'
            return render(request, 'form/salesToVendorForm.html', context)
    else:
        user = request.user
        form = SalesToVendorForm(user=user)
        context["form"] = form
        return render(request, 'form/salesToVendorForm.html', context)