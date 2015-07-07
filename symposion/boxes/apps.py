from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BoxesConfig(AppConfig):
    name = "symposion.boxes"
    verbose_name = _("Symposion Boxes")
