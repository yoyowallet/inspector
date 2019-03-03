import django_filters

from .forms import CheckRunFilterForm
from .models import CheckRun


class CheckRunFilter(django_filters.FilterSet):
    class Meta:
        model = CheckRun
        fields = ['environment', 'datacheck', 'user', 'status', 'result']
        form = CheckRunFilterForm
