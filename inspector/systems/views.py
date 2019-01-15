from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import System, Environment, Instance
from .forms import SystemForm, EnvironmentForm, InstanceForm


class SystemListView(ListView):
    model = System


class SystemCreateView(CreateView):
    model = System
    form_class = SystemForm


class SystemDetailView(DetailView):
    model = System


class SystemUpdateView(UpdateView):
    model = System
    form_class = SystemForm


class EnvironmentListView(ListView):
    model = Environment


class EnvironmentCreateView(CreateView):
    model = Environment
    form_class = EnvironmentForm


class EnvironmentDetailView(DetailView):
    model = Environment


class EnvironmentUpdateView(UpdateView):
    model = Environment
    form_class = EnvironmentForm


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
