from django import template
from upskill_photography.models import Picture

register = template.Library()

@register.inclusion_tag('upskill_photography/picture_thumbnail.html')
def get_picture_thumbnail(picture=None):
    width = picture.thumbnail.width
    height = picture.thumbnail.height
    return {'picture': picture, 'aspect_ratio': width/height}