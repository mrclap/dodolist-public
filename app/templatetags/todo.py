from django import template

register = template.Library()


@register.filter(name='complete_font_maker')
def transfer_complete(value):
    if value == 0:
        return 'check_box_outline_blank'
    else:
        return 'check'