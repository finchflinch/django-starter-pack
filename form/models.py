from django.db import models
from flow.models import Flow
from django.utils.translation import gettext_lazy as _

STATUS_CHOICES = [
    ("APPROVED", "Approved"),
    ("IN_PROCESS", "In Process"),
    ("REJECTED", "Rejected"),
    ("ON_HOLD", "On Hold"),
]


# Create your models here.
class SalesToVendor(models.Model):
    # on submit generated
    form_id = models.CharField(_("Form ID"), max_length=20)

    # user specific data
    company_code = models.CharField(_("Company Code"), max_length=5)

    sold_to_BP = models.CharField(_("Sold To BP"), max_length=50)
    ship_to_BP = models.CharField(_("Ship To BP"), max_length=50)
    order_series = models.CharField(_("Order Series"), max_length=50)
    order_type = models.CharField(_("Order Type"), max_length=50)
    sales_office = models.CharField(_("Sales Office"), max_length=50)
    area = models.CharField(_("Area"), max_length=50)
    postal_add_code = models.CharField(_("Postal Address Code"), max_length=200)
    del_add_code = models.CharField(_("Delivery Address Code"), max_length=200)
    order_discount = models.CharField(_("Order Discount"), max_length=50)
    warehouse = models.CharField(_("Warehouse"), max_length=50)
    pricelist = models.CharField(_("Pricelist"), max_length=50)
    payment_terms = models.CharField(_("Payment Terms"), max_length=50)
    ref_A1 = models.CharField(_("Reference A1"), max_length=50)
    ref_B1 = models.CharField(_("Reference B1"), max_length=50)
    header_text = models.CharField(_("Header Text"), max_length=50)
    ext_sales_rep = models.CharField(_("External Sales Rep Code"), max_length=50)
    int_sales_rep = models.CharField(_("Internal Sales Rep code"), max_length=50)
    planned_del_date = models.DateField(_("Planned Delivery Date"), auto_now=False, auto_now_add=False)
    planned_reciept_date = models.DateField(_("Planned Receipt Date"), auto_now=False, auto_now_add=False)
    date_created = models.DateField(_("Date Created"), auto_now=False, auto_now_add=True)

    # form metadata for managing flows
    status = models.CharField(_("Form Status"), max_length=15, choices=STATUS_CHOICES)
    reach_code = models.ForeignKey(Flow, on_delete=models.PROTECT)


