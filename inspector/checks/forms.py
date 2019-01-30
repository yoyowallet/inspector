from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import CheckGroup, Datacheck, CheckRun, EnvironmentStatus


class CreateCheckRunForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = CheckRun
        fields = ['environment']


class CheckGroupForm(forms.ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class="btn-sm"))

    class Meta:
        model = CheckGroup
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea({'cols': 40, 'rows': 3})
        }


class DatacheckForm(forms.ModelForm):
    class Meta:
        model = Datacheck
        fields = ['code', 'description', 'weight', 'left_system', 'left_type', 'left_logic', 'relation', 'right_system',
                  'right_type', 'right_logic',
                  'supports_warning', 'warning_relation', 'warning_type', 'warning_logic', 'group']


class CheckRunForm(forms.ModelForm):
    class Meta:
        model = CheckRun
        fields = ['start_time', 'end_time', 'status', 'result', 'left_value', 'right_value', 'warning_value',
                  'error_message', 'datacheck', 'environment', 'user']


class EnvironmentStatusForm(forms.ModelForm):
    class Meta:
        model = EnvironmentStatus
        fields = ['last_start_time', 'last_end_time', 'status', 'result', 'datacheck', 'environment', 'user']
