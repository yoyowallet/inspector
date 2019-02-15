from django.template import Library

register = Library()


@register.inclusion_tag('components/modals_modal.html')
def modals_modal(modal_id):
    return {'id': modal_id}


@register.inclusion_tag('components/modals_delete.js')
def modals_delete_js(object_type):
    return {'object': object_type}


@register.inclusion_tag('components/modals_run.js')
def modals_run_js(object_type):
    return {'object': object_type}
