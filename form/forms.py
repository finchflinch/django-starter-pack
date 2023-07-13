from django.forms import ModelForm, DateInput
from .models import SalesToVendor

class SalesToVendorForm(ModelForm):
    class Meta:
        model = SalesToVendor
        exclude = ["form_id", "date_created"]
        widgets = {
            'planned_del_date': DateInput(attrs={'type': 'date'}),
            'planned_reciept_date': DateInput(attrs={'type': 'date'}),
        }
        # fields = ["company_code","sold_to_BP", "ship_to_BP", "order_series", "order_type"]
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'field_to_exclude':
                field.required = True
        self.fields['company_code'].initial = user.company
        self.fields['company_code'].widget.attrs['readonly'] = True
        # self.fields['reach_code']
