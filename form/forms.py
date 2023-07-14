from django.forms import ModelForm, DateInput, Select, TextInput
from .models import SalesToVendor, Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["comment_date", "form_id", "flow_type", "commentor"]
        widgets = {
            'action': Select(attrs={'class': 'form-control', 'required': True}),
            'remark': TextInput(attrs={'placeholder': 'Enter remarks', 'required': True})
        }


class SalesToVendorForm(ModelForm):
    class Meta:
        model = SalesToVendor
        exclude = ["form_id", "date_created", "reach_code", "status"]
        widgets = {
            'planned_del_date': DateInput(attrs={'type': 'date'}),
            'planned_reciept_date': DateInput(attrs={'type': 'date'}),
        }
        # fields = ["company_code","sold_to_BP", "ship_to_BP", "order_series", "order_type"]
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        if user.role.role_name == 'PLANT STORE':
            for field_name, field in self.fields.items():
                if field_name != 'field_to_exclude':
                    field.required = True
            self.fields['company_code'].initial = user.company
            self.fields['company_code'].widget.attrs['readonly'] = True
        elif user.role.role_name == 'PLANNING':
            for field_name, field in self.fields.items():
                self.fields[field_name].widget.attrs['readonly'] = True
