from django import template

register = template.Library()

@register.filter(name='cut')   #doing that with text decorator instead of writing line 12
def cut(value, arg):

    """ This cuts out all the values of "arg" rom the string """

    return value.replace(arg,'')

# register.filter('cut', cut)
