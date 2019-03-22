import django_filters

from .forms import CheckRunFilterForm, EnvironmentStatusFilterForm
from .models import CheckRun, EnvironmentStatus


class CheckRunFilter(django_filters.FilterSet):
    class Meta:
        model = CheckRun
        fields = ['environment', 'datacheck', 'user', 'status', 'result']
        form = CheckRunFilterForm


class EnvironmentStatusFilter(django_filters.FilterSet):
    class Meta:
        model = EnvironmentStatus
        fields = ['environment', 'datacheck', 'user', 'status', 'result']
        form = EnvironmentStatusFilterForm
