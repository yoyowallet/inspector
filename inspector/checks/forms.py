from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from crispy_forms.bootstrap import TabHolder, Tab, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Field, HTML
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


def prepended_select_column(field: str, width: int, extra_classes: str = ''):
    return Column(
        Field(field,
              template="components/forms/select_prepend.html"
              ),
        css_class=f'form-group col-md-{width} {extra_classes}')


class DatacheckForm(forms.ModelForm):
    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Column(PrependedText(
                'code', 'Check code',
                template="components/forms/prepended_appended_text.html"),
                css_class='form-group col-md-5 mb-0 mt-2'),
            Column(None, css_class='col-md-1'),
            prepended_select_column('group', 3, 'mb-0 mt-2'),
            Column(None, css_class='col-md-1'),
            Column(
                PrependedText(
                    'weight', '<i class="fas fa-balance-scale" title="Weight"></i>',
                    template="components/forms/prepended_appended_text.html"),
                css_class='input-group-sm col-md-2 mb-0 mt-2'),
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
                    prepended_select_column('left_system', 3, 'm-1'),
                    prepended_select_column('left_type', 3, 'm-1'),
                ),
                Row(
                    Column('left_logic', css_class='form-group col-md-12 mb-0')
                )
            ),
            Tab('Right',
                Row(
                    prepended_select_column('relation', 2, 'm-1'),
                    prepended_select_column('right_system', 3, 'm-1'),
                    prepended_select_column('right_type', 3, 'm-1'),
                ),
                Row(
                    Column('right_logic', css_class='form-group col-md-12 mb-0')
                )
                ),
            Tab('Warning',
                Row(
                    Column('supports_warning', css_class='form-group col-md-1 mb-0 mt-1'),
                    prepended_select_column('warning_relation', 2, 'm-1'),
                    prepended_select_column('warning_type', 3, 'm-1')
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
        system_icon = '<i class="fas fa-desktop" title="System"></i>'
        logic_icon = '<i class="fas fa-code" title="Logic"></i>'
        group_icon = '<i class="far fa-object-ungroup" title="Group"></i>'
        labels = {
            'left_system': system_icon,
            'left_type': 'Type',
            'left_logic': logic_icon,
            'right_system': system_icon,
            'right_type': 'Type',
            'right_logic': logic_icon,
            'warning_type': 'Type',
            'warning_relation': 'Relation',
            'warning_logic': logic_icon,
            'supports_warning': 'Enabled',
            'code': False,
            'weight': False,
            'group': group_icon
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
            prepended_select_column('datacheck', 5, 'mb-1'),
            prepended_select_column('environment', 3, 'mb-1'),
            prepended_select_column('status', 2, 'mb-1'),
            prepended_select_column('result', 2, 'mb-1')
        ), Row(
            prepended_select_column('user', 3, 'mb-1'),
            Column(
                Submit('submit', 'Search', css_class=SUBMIT_CSS_CLASSES),
                css_class='form-group col-md-1 mb-1'),
            Column(
                HTML("""
                <a class="btn btn-outline-danger btn-block btn-sm"
                href={% url "checks_checkrun_list" %}>Reset</a>
                """),
                css_class='form-group col-md-1 mb-1'),
            css_class='form-row'
        )
    )

    class Meta:
        model = CheckRun
        fields = ['datacheck', 'environment', 'user', 'status', 'result']


class EnvironmentStatusFilterForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'GET'
    helper.layout = Layout(
        Row(
            prepended_select_column('environment', 2, 'mb-0'),
            prepended_select_column('datacheck', 4, 'mb-0'),
            prepended_select_column('status', 2, 'mb-0'),
            prepended_select_column('result', 2, 'mb-0'),
            Column(
                Submit('submit', 'Search', css_class=SUBMIT_CSS_CLASSES),
                css_class='form-group col-md-1 mb-0'),
            Column(
                HTML("""
                <a class="btn btn-outline-danger btn-block btn-sm"
                href={% url "checks_environmentstatus_list" %}>Reset</a>
                """),
                css_class='form-group col-md-1 mb-0'),
            css_class='form-row'
        )
    )

    class Meta:
        model = EnvironmentStatus
        fields = ['environment', 'datacheck', 'status', 'result']
