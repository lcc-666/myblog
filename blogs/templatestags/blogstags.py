from django import template
from blogs.models import Blogs

register = template.Library()


@register.simple_tag
def get_top_blogs():
    hotblogs = Blogs.objects.filter(isTop=True)
    return hotblogs

@register.simple_tag
def get_date_list():
    return Blogs.objects.dates('createtime','month',order='DESC')

