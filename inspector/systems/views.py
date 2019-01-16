from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView, CreateView

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


class InstanceCreateView(CreateView):
    model = Instance
    form_class = InstanceForm


class InstanceDetailView(DetailView):
    model = Instance


class InstanceUpdateView(UpdateView):
    model = Instance
    form_class = InstanceForm
