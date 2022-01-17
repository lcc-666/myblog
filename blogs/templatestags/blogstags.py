from django import template
from blogs.models import Blogs,Tags

register = template.Library()


@register.simple_tag
def get_top_blogs():
    hotblogs = Blogs.objects.filter(isTop=True)
    return hotblogs

@register.simple_tag
def get_date_list():
    return Blogs.objects.dates('createtime','month',order='DESC')

@register.simple_tag
def get_tags_list():
    return Tags.objects.all()
