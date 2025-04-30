from django import template
from django.apps import apps

register = template.Library()

@register.filter
def admin_count(_, model_label):
    try:
        app_label, model_name = model_label.split('.')
        Model = apps.get_model(app_label, model_name)
        return Model.objects.count()
    except Exception:
        return '-' 