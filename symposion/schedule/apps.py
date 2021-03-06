from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ScheduleConfig(AppConfig):
    name = "symposion.schedule"
    label = "symposion_schedule"
    verbose_name = _("Symposion Schedule")
