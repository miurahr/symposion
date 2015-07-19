from __future__ import unicode_literals
from collections import OrderedDict

from django import forms

import account.forms
from django.utils.translation import ugettext_lazy as _


class SignupForm(account.forms.SignupForm):

    first_name = forms.CharField(label=_("First name"))
    last_name = forms.CharField(label=_("Last name"))
    email_confirm = forms.EmailField(label=_("Confirm Email"))

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]
        key_order = [
            "email",
            "email_confirm",
            "first_name",
            "last_name",
            "password",
            "password_confirm"
        ]
        self.fields = reorder_fields(self.fields, key_order)

    def clean_email_confirm(self):
        email = self.cleaned_data.get("email")
        email_confirm = self.cleaned_data["email_confirm"]
        if email:
            if email != email_confirm:
                raise forms.ValidationError(
                    _("Email address must match previously typed email address"))
        return email_confirm


def reorder_fields(fields, order):
    """Reorder form fields by order, removing items not in order.

    >>> reorder_fields(
    ...     OrderedDict([('a', 1), ('b', 2), ('c', 3)]),
    ...     ['b', 'c', 'a'])
    OrderedDict([('b', 2), ('c', 3), ('a', 1)])
    """
    for key, v in fields.items():
        if key not in order:
            del fields[key]

    return OrderedDict(sorted(fields.items(), key=lambda k: order.index(k[0])))
