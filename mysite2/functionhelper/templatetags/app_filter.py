from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter(name='lookup')
def lookup(d, key):
    return d[key]

register.filter(lookup)