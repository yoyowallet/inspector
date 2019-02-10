from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from inspector.taskapp.tasks import execute_check
from .constants import STATUSES
from .forms import CreateCheckRunForm, CheckGroupForm, DatacheckForm
from .models import Datacheck, CheckGroup, CheckRun, EnvironmentStatus


class CheckListView(ListView):
    model = Datacheck
    slug_field = "code"
    slug_url_kwarg = "code"


check_list_view = CheckListView.as_view()


class DatacheckDetailView(DetailView):
    model = Datacheck
    template_name = 'checks/datacheck_detail.html'


check_detail_view = DatacheckDetailView.as_view()


class CheckRunCreateView(PassRequestMixin, SuccessMessageMixin,
                         CreateView):
    template_name = 'checks/checkrun_create.html'
    form_class = CreateCheckRunForm
    success_message = 'Success: Check was triggered.'
    success_url = reverse_lazy('checks_datacheck_list')

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


class DatacheckDeleteView(DeleteAjaxMixin, DeleteView):
    model = Datacheck
    template_name = 'components/modals_delete.html'
    success_message = 'Success: Check was deleted.'
    success_url = reverse_lazy('checks_datacheck_list')


check_delete_view = DatacheckDeleteView.as_view()


class CheckGroupListView(ListView):
    model = CheckGroup


class CheckGroupCreateView(CreateView):
    model = CheckGroup
    form_class = CheckGroupForm

    def get_success_url(self):
        return reverse('checks_checkgroup_list')


class CheckGroupUpdateView(UpdateView):
    model = CheckGroup
    form_class = CheckGroupForm

    def get_success_url(self):
        return reverse('checks_checkgroup_list')


class CheckRunListView(ListView):
    model = CheckRun
    paginate_by = 50

    def get_paginate_by(self, queryset):
        """
        Paginate by specified value in querystring, or use default class property value.
        """
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        return CheckRun.objects.select_related()


class CheckRunDetailView(DetailView):
    model = CheckRun


class DatacheckCreateView(CreateView):
    model = Datacheck
    form_class = DatacheckForm


class DatacheckUpdateView(UpdateView):
    model = Datacheck
    form_class = DatacheckForm


class EnvironmentStatusListView(ListView):
    model = EnvironmentStatus


class CheckGroupDeleteView(DeleteAjaxMixin, DeleteView):
    model = CheckGroup
    template_name = 'components/modals_delete.html'
    success_message = 'Success: Check group was deleted.'
    success_url = reverse_lazy('checks_checkgroup_list')


class DatacheckInfoView(DetailView):
    model = Datacheck
    template_name = 'checks/datacheck_info.html'
