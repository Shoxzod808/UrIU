# myapp/templatetags/my_tags.py
from django import template
from ..utils import get_text

register = template.Library()

@register.simple_tag
def call_get_text(title, lang, button=False):
    return get_text(title, lang, button)
