from django import forms


class InstanceForm(forms.ModelForm):
    class Meta:
        widgets = {
            'password': forms.PasswordInput()
        }
