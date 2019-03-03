from bootstrap_modal_forms.mixins import DeleteAjaxMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from .forms import SystemForm, EnvironmentForm, InstanceForm
from .models import System, Environment, Instance


class SystemListView(ListView):
    model = System


class SystemCreateView(CreateView):
    model = System
    form_class = SystemForm

    def get_success_url(self):
        return reverse('systems_system_list')


class SystemUpdateView(UpdateView):
    model = System
    form_class = SystemForm

    def get_success_url(self):
        return reverse('systems_system_list')


class EnvironmentListView(ListView):
    model = Environment


class EnvironmentCreateView(CreateView):
    model = Environment
    form_class = EnvironmentForm

    def get_success_url(self):
        return reverse('systems_environment_list')


class EnvironmentUpdateView(UpdateView):
    model = Environment
    form_class = EnvironmentForm

    def get_success_url(self):
        return reverse('systems_environment_list')


class InstanceListView(ListView):
    model = Instance

    def get_queryset(self):
        return Instance.objects.select_related()


class InstanceCreateView(CreateView):
    model = Instance
    form_class = InstanceForm

    def get_success_url(self):
        return reverse('systems_instance_list')


class InstanceDetailView(DetailView):
    model = Instance


class InstanceUpdateView(UpdateView):
    model = Instance
    form_class = InstanceForm


class SystemDeleteView(DeleteAjaxMixin, DeleteView):
    model = System
    template_name = 'components/modals_delete.html'
    success_message = 'Success: System was deleted.'
    success_url = reverse_lazy('systems_system_list')


class EnvironmentDeleteView(DeleteAjaxMixin, DeleteView):
    model = Environment
    template_name = 'components/modals_delete.html'
    success_message = 'Success: Environment was deleted.'
    success_url = reverse_lazy('systems_environment_list')


class InstanceDeleteView(DeleteAjaxMixin, DeleteView):
    model = Instance
    template_name = 'components/modals_delete.html'
    success_message = 'Success: Instance was deleted.'
    success_url = reverse_lazy('systems_instance_list')
