from django.template import Library
import math

register = Library()

@register.filter
def divide(dividendo,divisor):
    value=0
    if divisor !=0:
        value=dividendo/divisor
        value=round(value,2)
    
    return(value)

@register.filter
def solo_decimal(decimal):
    parte_decimal, parte_entera = math.modf(decimal)
    parte_decimal=round(parte_decimal,2)
    parte_decimal=str(parte_decimal)
    parte_decimal=parte_decimal.lstrip('0,')
    return parte_decimal


@register.filter
def solo_entero(decimal):
    parte_decimal, parte_entera = math.modf(decimal)
    
    return int(parte_entera)