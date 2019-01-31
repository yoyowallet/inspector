from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from django import forms

from .models import Environment, Instance, System


class SystemForm(forms.ModelForm):
    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Column('name', css_class='form-group col-md-6 mb-0'),
            Column('application', css_class='form-group col-md-6 mb-0'),
            css_class='form-row'
        ),
        Submit('submit', 'Submit', css_class="btn-sm"))

    class Meta:
        model = System
        fields = ['name', 'application']


class EnvironmentForm(forms.ModelForm):
    class Meta:
        model = Environment
        fields = ['name']


class InstanceForm(forms.ModelForm):
    class Meta:
        model = Instance
        fields = ['system', 'environment', 'host', 'port', 'database_or_schema', 'login', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Column('system', css_class='form-group col-md-6 mb-0'),
            Column('environment', css_class='form-group col-md-6 mb-0'),
            css_class='form-row'
        ),
        Row(
            Column('host', css_class='form-group col-md-8 mb-0'),
            Column('port', css_class='form-group col-md-1 mb-0'),
            Column('database_or_schema', css_class='form-group col-md-3 mb-0'),
            css_class='form-row'
        ),
        Row(
            Column('login', css_class='form-group col-md-6 mb-0'),
            Column('password', css_class='form-group col-md-6 mb-0'),
            css_class='form-row'
        ),
        Submit('submit', 'Submit', css_class="btn-sm"))
