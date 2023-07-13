from django.urls import path, include
from . import views

urlpatterns = [
    path("sales_to_vendor_form/", views.sales_to_vendor_form, name="sales_to_vendor_form"),
]
