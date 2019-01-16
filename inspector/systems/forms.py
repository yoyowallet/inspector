from django import forms

from .models import Environment, Instance, System


class SystemForm(forms.ModelForm):
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
