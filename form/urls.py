from django.urls import path, include
from . import views

urlpatterns = [
    path("sales_to_vendor_form/", views.sales_to_vendor_form, name="sales_to_vendor_form"),
    path("sales_to_vendor_form/<str:form_id>/", views.sales_to_vendor_approval, name="sales_to_vendor_approval"),
    path('comment/<str:form_id>/', views.comment, name='comment'),
]
