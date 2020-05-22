from django import template

register = template.Library()

@register.filter()
def quantity_producto_format(quantity=1):
    return '{} {}'.format(quantity, 'productos' if quantity > 1 else 'producto')

@register.filter()
def quantity_add_format(quantity=1):
    return '{} {}'.format(
        quantity_producto_format(quantity),
        'agregados' if quantity > 1 else 'agregado'
    )