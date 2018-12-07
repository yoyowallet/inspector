from django.contrib import admin

from .forms import InstanceForm
from .models import System, Enviroment, Instance


class SystemsAdmin(admin.ModelAdmin):
    list_display = ('name',)


class InstanceAdmin(admin.ModelAdmin):
    form = InstanceForm


admin.site.register(System, SystemsAdmin)
admin.site.register(Enviroment)
admin.site.register(Instance, InstanceAdmin)
