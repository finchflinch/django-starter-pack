from django.db import models
from user.models import Role
from django.utils.translation import gettext_lazy as _


# Create your models here.
class FlowName(models.Model):
    flow_name = models.CharField(_("name of flow"), max_length=200)
    flow_abbr = models.CharField(_('Flow Name Abbreviation'), max_length=3, unique=True, blank=True)

    def __str__(self):
        return f"{self.flow_name}"

    def test_create(self):
        test_obj = FlowName("TestFlow1")
        test_obj.save


class Flow(models.Model):
    flow_name = models.ForeignKey(FlowName, on_delete=models.PROTECT, default=1)
    reach_code = models.IntegerField(_("Reach Code"), unique=False)
    pending_at_role = models.ForeignKey(
        Role, verbose_name=_("Pending at role"), on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.flow_name}_{self.reach_code}_{self.pending_at_role}"
