from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from django import forms

from .models import Environment, Instance, System
from ..base.constants import SUBMIT_CSS_CLASSES


class SystemForm(forms.ModelForm):
    helper = FormHelper()
    helper.add_input(Submit("submit", "Submit", css_class=SUBMIT_CSS_CLASSES))

    class Meta:
        model = System
        fields = ["name", "application"]


class EnvironmentForm(forms.ModelForm):
    class Meta:
        model = Environment
        fields = ["name"]

    helper = FormHelper()
    helper.add_input(Submit("submit", "Submit", css_class=SUBMIT_CSS_CLASSES))


class InstanceForm(forms.ModelForm):
    class Meta:
        model = Instance
        fields = [
            "system",
            "environment",
            "host",
            "port",
            "db",
            "schema",
            "login",
            "password",
            "extra_json",
        ]
        widgets = {
            "password": forms.PasswordInput(),
            "extra_json": forms.Textarea({"cols": 40, "rows": 3}),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Column("system", css_class="form-group col-md-6 mb-0"),
            Column("environment", css_class="form-group col-md-6 mb-0"),
            css_class="form-row",
        ),
        Row(
            Column("host", css_class="form-group col-md-10 mb-0"),
            Column("port", css_class="form-group col-md-2 mb-0"),
            css_class="form-row",
        ),
        Row(
            Column("db", css_class="form-group col-md-6 mb-0"),
            Column("schema", css_class="form-group col-md-6 mb-0"),
            css_class="form-row",
        ),
        Row(
            Column("login", css_class="form-group col-md-6 mb-0"),
            Column("password", css_class="form-group col-md-6 mb-0"),
            css_class="form-row",
        ),
        Row(
            Column("extra_json", css_class="form-group col-md-12 mb-0"),
            css_class="form-row",
        ),
        Submit("submit", "Submit", css_class="btn-sm"),
    )
