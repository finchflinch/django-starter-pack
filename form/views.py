from django.shortcuts import render
from .forms import SalesToVendorForm

# Create your views here.
def sales_to_vendor_form(request):
    context = {}
    if request.method == 'POST':
        form = SalesToVendorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        user = request.user
        form = SalesToVendorForm(request.POST or None, user=user)
        context["form"] = form
        return render(request, 'form/salesToVendorForm.html', context)