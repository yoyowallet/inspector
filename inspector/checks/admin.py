from django.contrib import admin

from .models import Datacheck, CheckGroup


class CheckGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


class DatacheckAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('code', 'description', 'group', 'weight')}),
        ('Left', {'fields': ('left_system', 'left_type', 'left_logic')}),
        ('Relation', {'fields': ('relation',)}),
        ('Right', {'fields': ('right_system', 'right_type', 'right_logic')}),
        ('Warning', {'fields': ('supports_warning', 'warning_type', 'warning_logic')})
    )


admin.site.register(Datacheck, DatacheckAdmin)
admin.site.register(CheckGroup, CheckGroupAdmin)
