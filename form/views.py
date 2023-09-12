from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
import secrets
import string
from .forms import SalesToVendorForm, CommentForm
from .models import SalesToVendor, Comment
from flow.models import FlowName, Flow

def unique_id(flow_abbr, form_id):
    #           6_3(max)_3(max)_5
    # template: YYMMDD_FLOWNAMEABBR_formID__random
    characters = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(characters) for _ in range(5))
    yymmdd = timezone.now().strftime("%y%m%d")
    abbr = flow_abbr
    id = form_id
    return f"{yymmdd}_{abbr}_{id}_{random_string}"

# Create your views here.
@login_required
def comment(request, form_id):
    context = {}
    if request.method == 'POST':
        user = request.user
        comment = CommentForm(request.POST)
        if comment.is_valid():
            flow_type_abbr = form_id.split('_')[1]
            flow_type = FlowName.objects.get(flow_abbr=flow_type_abbr)
            comment.instance.form_id = form_id
            comment.instance.flow_type= flow_type
            comment.instance.commentor = user
            comment.save()
            # perform the logics of all actions
            form = SalesToVendor.objects.get(form_id=form_id)
            # if approved, check if approval was final or intermediate
            if comment.instance.action == 'APPROVED':
                commentor_level = Flow.objects.get(flow_name=flow_type, pending_at_role=user.role)
                final_level = Flow.objects.filter(flow_name=flow_type).order_by('-reach_code').first()
                
                '''
                # custom logic here
                # compare value here to pass it to plant head
                
                '''
                if commentor_level.reach_code < final_level.reach_code:
                    # assign the next reach code
                    new_form_reach_code = Flow.objects.get(flow_name=flow_type, 
                                                           reach_code=commentor_level.reach_code + 1)
                    form.reach_code = new_form_reach_code
                    form.save()
                elif commentor_level.reach_code == final_level.reach_code:
                    form.status = 'APPROVED'
                    form.save()
            elif comment.instance.action == 'REJECTED':
                form.status = 'REJECTED'
                form.save()
        return redirect('home')
        # return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def sales_to_vendor_approval(request, form_id):
    context = {}
    if request.method == 'POST':
        pass
    else:
        # first check if form exists
        user = request.user
        flow_type_abbr = form_id.split('_')[1]
        if flow_type_abbr == 'STV':
            form_queryset = SalesToVendor.objects.filter(form_id=form_id).exclude(status__in=['REJECTED', 'APPROVED'])
            if len(form_queryset) == 0:
                return redirect('home')
            else:
                # check if the user is the currently assigned 
                form = SalesToVendorForm(instance=form_queryset[0], user=user)
                context['form'] = form
                context['form_id'] = form_id
                # logics specific to users
                if user.role.role_name in ["PLANNING"]:
                    context["form_editable"] = False
                # only allow commenting option if 
                # reach_code and company code is of user
                if user.role == form_queryset[0].reach_code.pending_at_role and user.company == form_queryset[0].company_code:
                    comment = CommentForm()
                    context["comment"] = comment
                # show comments
                all_comments = Comment.objects.filter(form_id=form_id).order_by('-comment_date')
                context['all_comments'] = all_comments
        return render(request, 'form/approval.html', context)

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
            model_instance = form.save()

            form_id = unique_id(flow_type.flow_abbr, model_instance.id)
            model_instance.form_id = form_id
            model_instance.save()

            context['msg'] = 'form saved successfully'
            return render(request, 'form/salesToVendorForm.html', context)
    else:
        user = request.user
        form = SalesToVendorForm(user=user)
        context["form"] = form
        return render(request, 'form/salesToVendorForm.html', context)