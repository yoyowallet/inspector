from django import template

register = template.Library()


@register.inclusion_tag('components/button_edit.html')
def button_edit(instance):
    return {'url': instance.get_update_url()}
