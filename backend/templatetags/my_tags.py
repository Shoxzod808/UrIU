# myapp/templatetags/my_tags.py
from django import template
from ..utils import get_text

register = template.Library()

@register.simple_tag
def call_get_text(arg):
    return get_text(arg)
