from collections import OrderedDict
from distutils.version import StrictVersion

from django import forms, get_version

import account.forms


class SignupForm(account.forms.SignupForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email_confirm = forms.EmailField(label="Confirm Email")

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
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
                    "Email address must match previously typed email address")
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

    if StrictVersion(get_version()) < StrictVersion('1.7.0'):
        # fields is SortedDict
        fields.keyOrder.sort(key=lambda k: order.index(k[0]))
        return fields
    else:
        # fields is OrderedDict
        return OrderedDict(sorted(fields.items(), key=lambda k: order.index(k[0])))
