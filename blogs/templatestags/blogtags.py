from django import template
from blogs.models import Blogs

register = template.Library


@register.simple_tag
def get_top_blogs():
    hotblogs = Blogs.objects.filter(isTop=True)
    return hotblogs
