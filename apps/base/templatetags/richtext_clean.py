from django import template
register = template.Library()


@register.filter()
def richtext_clean(data):
    # split me devuelve una list de dos elementos, tomo el segundo y utilizo replace para reemplazar la etiqueta
    data_convert = data.split(">")[1].replace('</p', '')
    return data_convert

register.filter("richtext_clean", richtext_clean)
