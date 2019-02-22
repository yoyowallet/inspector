import django_filters

from .models import CheckRun


class CheckRunFilter(django_filters.FilterSet):

    class Meta:
        model = CheckRun
        fields = ['environment', 'datacheck', 'user']
