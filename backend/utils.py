# myapp/utils.py
from .models import Template, Template2Button


def get_text(title, lang, button=False):
    try:
        if button:
            text = Template2Button.objects.get(title=title)
        else:
            text = Template.objects.get(title=title)
        if lang == 'ru':
            text = text.body_ru
        elif lang == 'en':
            text = text.body_en
        else:
            text = text.body_uz
    except Exception:
        text = f'Шаблон: {title} не найден!!! '
    return text
