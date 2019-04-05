import django_filters

from .forms import CheckRunFilterForm, EnvironmentStatusFilterForm
from .models import CheckRun, EnvironmentStatus


class CheckRunFilter(django_filters.FilterSet):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['environment'].label = ICON_ENVIRONMENT
        self.filters['datacheck'].label = ICON_DATACHECK
        self.filters['status'].label = ICON_STATUS
        self.filters['user'].label = ICON_USER
        self.filters['result'].label = ICON_RESULT

    start_time = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = CheckRun
        fields = ['environment', 'datacheck', 'user', 'status', 'result', 'start_time']
        form = CheckRunFilterForm


class EnvironmentStatusFilter(django_filters.FilterSet):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['environment'].label = ICON_ENVIRONMENT
        self.filters['datacheck'].label = ICON_DATACHECK
        self.filters['status'].label = ICON_STATUS
        self.filters['result'].label = ICON_RESULT

    class Meta:
        model = EnvironmentStatus
        fields = ['environment', 'datacheck', 'status', 'result']
        form = EnvironmentStatusFilterForm


ICON_DATACHECK = '<i class="fas fa-list" title="Check code"></i>'
ICON_ENVIRONMENT = '<i class="fas fa-globe-africa" title="Environment"></i>'
ICON_STATUS = '<i class="far fa-clock" title="Status"></i>'
ICON_RESULT = '<i class="fas fa-question" title="Result"></i>'
ICON_USER = '<i class="fas fa-user-cog" title="User"></i>'
