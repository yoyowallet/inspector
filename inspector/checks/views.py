from datetime import datetime as dt

import pytz
from bootstrap_modal_forms.mixins import PassRequestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from inspector.taskapp.tasks import execute_check
from .constants import STATUSES
from .forms import CreateCheckRunForm
from .models import Datacheck


class CheckListView(ListView):
    model = Datacheck
    slug_field = "code"
    slug_url_kwarg = "code"


check_list_view = CheckListView.as_view()


class CheckDetailView(DetailView):
    model = Datacheck
    slug_field = "code"
    slug_url_kwarg = "code"


check_detail_view = CheckDetailView.as_view()


class CheckRunCreateView(PassRequestMixin, SuccessMessageMixin,
                         CreateView):
    template_name = 'checks/checkrun_create.html'
    form_class = CreateCheckRunForm
    success_message = 'Success: Check was triggered.'
    success_url = reverse_lazy('checks:index')

    def form_valid(self, form):
        form.instance.datacheck_id = self.kwargs['check_id']
        form.instance.user = self.request.user
        form.instance.status = STATUSES.NEW
        # TODO - check if system is available in environment

        return super().form_valid(form)

    def get_success_url(self):
        check_run_id = self.object.id
        if check_run_id is not None:
            execute_check.delay(check_run_id)
        return super().get_success_url()


checkrun_create_view = CheckRunCreateView.as_view()
