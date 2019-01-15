from django import forms

from .models import System, Environment, Instance


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
        fields = ['host', 'port', 'database_or_schema', 'login', 'password', 'system', 'environment']
        widgets = {
            'password': forms.PasswordInput()
        }
