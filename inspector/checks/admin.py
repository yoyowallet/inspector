from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Datacheck, CheckGroup


class CheckGroupAdmin(admin.ModelAdmin):
    list_display = ("name",)


class DatacheckResource(resources.ModelResource):
    class Meta:
        model = Datacheck


class DatacheckAdmin(ImportExportModelAdmin):
    fieldsets = (
        (None, {"fields": ("code", "description", "group", "weight")}),
        ("Left", {"fields": ("left_system", "left_type", "left_logic")}),
        ("Relation", {"fields": ("relation",)}),
        ("Right", {"fields": ("right_system", "right_type", "right_logic")}),
        ("Warning", {"fields": ("supports_warning", "warning_type", "warning_logic")}),
    )
    resource_class = DatacheckResource


admin.site.register(Datacheck, DatacheckAdmin)
admin.site.register(CheckGroup, CheckGroupAdmin)
