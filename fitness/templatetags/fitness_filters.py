from django import template

register = template.Library()

@register.filter
def div(value, arg):
    try:
        return round(value / arg * 100)
    except (ZeroDivisionError, TypeError):
        return 0

@register.filter
def mul(value, arg):
    return round(value * arg)