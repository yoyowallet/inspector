from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms

from .models import CheckGroup, Datacheck, CheckRun, EnvironmentStatus


class CreateCheckRunForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = CheckRun
        fields = ['environment']


class CheckGroupForm(forms.ModelForm):
    class Meta:
        model = CheckGroup
        fields = ['name', 'description']


class DatacheckForm(forms.ModelForm):
    class Meta:
        model = Datacheck
        fields = ['code', 'description', 'weight', 'left_type', 'left_logic', 'relation', 'right_logic',
                  'supports_warning', 'warning_relation', 'warning_type', 'warning_logic', 'group', 'left_system',
                  'right_system']


class CheckRunForm(forms.ModelForm):
    class Meta:
        model = CheckRun
        fields = ['start_time', 'end_time', 'status', 'result', 'left_value', 'right_value', 'warning_value',
                  'error_message', 'datacheck', 'environment', 'user']


class EnvironmentStatusForm(forms.ModelForm):
    class Meta:
        model = EnvironmentStatus
        fields = ['last_start_time', 'last_end_time', 'status', 'result', 'datacheck', 'environment', 'user']
