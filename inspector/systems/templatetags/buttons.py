from django.template import Library, loader
from django.urls import reverse
from django.utils.html import escape, mark_safe

register = Library()


@register.inclusion_tag('components/button_edit.html')
def button_edit(instance):
    return {'url': instance.get_update_url()}


@register.inclusion_tag('components/button_new.html')
def button_new(url_name):
    return {'url': reverse(url_name)}


@register.inclusion_tag('components/button_detail.html')
def button_detail(instance):
    return {'url': instance.get_absolute_url()}


@register.simple_tag(takes_context=True)
def button_hoverdetail(context, template_name, instance):
    hover_template = loader.get_template(f'{template_name}.html')
    hover_content = hover_template.render({'object': instance})

    button_template = loader.get_template('components/button_hoverdetail.html')
    return button_template.render({'content': escape(hover_content)})


@register.simple_tag
def button_submit():
    return mark_safe("""<button class="btn btn-primary btn-sm" type="submit">Submit</button>""")


@register.inclusion_tag('components/button_delete.html')
def button_delete(instance):
    return {
        'url': instance.get_delete_url(),
        'delete_class': f'{instance.__class__.__name__.lower()}-delete',
        'name': instance.get_name()
    }
