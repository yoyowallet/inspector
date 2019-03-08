from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from django import forms
from djangocodemirror.widgets import CodeMirrorWidget

from .models import CheckGroup, Datacheck, CheckRun, EnvironmentStatus
from ..base.constants import SUBMIT_CSS_CLASSES


class DatacheckRunForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = CheckRun
        fields = ['environment']


class CheckGroupRunForm(PopRequestMixin, forms.ModelForm):
    class Meta:
        model = CheckRun
        fields = ['environment']


class CheckGroupForm(forms.ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class=SUBMIT_CSS_CLASSES))

    class Meta:
        model = CheckGroup
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea({'cols': 40, 'rows': 3})
        }


class DatacheckForm(forms.ModelForm):
    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Column('code', css_class='form-group col-md-5 mb-0'),
            Column(None, css_class='col-md-2'),
            Column('group', css_class='form-group col-md-2 mb-0'),
            Column(None, css_class='col-md-2'),
            Column('weight', css_class='form-group col-md-1 mb-0'),
            css_class='form-row'
        ),
        Row(
            Column('description', css_class='form-group col-md-12 mb-0'),
            css_class='form-row'
        ),
        TabHolder(
            Tab(
                'Left',
                Row(
                    Column('left_system', css_class='form-group col-md-2 mb-0'),
                    Column('left_type', css_class='form-group col-md-2 mb-0')
                ),
                Row(
                    Column('left_logic', css_class='form-group col-md-12 mb-0')
                )
            ),
            Tab('Right',
                Row(
                    Column('relation', css_class='form-group col-md-2 mb-0'),
                    Column('right_system', css_class='form-group col-md-2 mb-0'),
                    Column('right_type', css_class='form-group col-md-2 mb-0')
                ),
                Row(
                    Column('right_logic', css_class='form-group col-md-12 mb-0')
                )
                ),
            Tab('Warning',
                Row(
                    Column('supports_warning', css_class='form-group col-md-1 mb-0'),
                    Column('warning_relation', css_class='form-group col-md-2 mb-0'),
                    Column('warning_type', css_class='form-group col-md-2 mb-0')
                ),
                Row(
                    Column('warning_logic', css_class='form-group col-md-12 mb-0')
                ))),
        Submit('submit', 'Submit', css_class="btn-sm")
    )

    class Meta:
        model = Datacheck
        fields = ['code', 'description', 'weight', 'left_system', 'left_type', 'left_logic', 'relation', 'right_system',
                  'right_type', 'right_logic',
                  'supports_warning', 'warning_relation', 'warning_type', 'warning_logic', 'group']
        widgets = {
            'description': forms.Textarea({'cols': 40, 'rows': 3}),
            'left_logic': CodeMirrorWidget(config_name='inspector'),
            'right_logic': CodeMirrorWidget(config_name='inspector'),
            'warning_logic': CodeMirrorWidget(config_name='inspector')
        }


class CheckRunForm(forms.ModelForm):
    class Meta:
        model = CheckRun
        fields = ['start_time', 'end_time', 'status', 'result', 'left_value', 'right_value', 'warning_value',
                  'error_message', 'datacheck', 'environment', 'user']


class EnvironmentStatusForm(forms.ModelForm):
    class Meta:
        model = EnvironmentStatus
        fields = ['last_start_time', 'last_end_time', 'status', 'result', 'datacheck', 'environment', 'user']


class CheckRunFilterForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'GET'
    helper.layout = Layout(
        Row(
            Column('datacheck', css_class='form-group col-md-4 mb-0'),
            Column('environment', css_class='form-group col-md-2 mb-0'),
            Column('status', css_class='form-group col-md-2 mb-0'),
            Column('result', css_class='form-group col-md-2 mb-0'),
            Column('user', css_class='form-group col-md-2 mb-0'),
            Submit('submit', 'Submit', css_class=SUBMIT_CSS_CLASSES),
            css_class='form-row'
        )
    )

    class Meta:
        model = CheckRun
        fields = ['datacheck', 'environment', 'user', 'status', 'result']
