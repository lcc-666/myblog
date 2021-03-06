from django.contrib import admin
from blogs.models import *

admin.site.site_header = "个人博客管理系统"
admin.site.site_title = "个人博客管理系统"

class TypeAdmin(admin.ModelAdmin):
    list_display = ['name','describe']


class TagsAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe']

class BlogsAdmin(admin.ModelAdmin):
    list_display = ['title','abstract','blogtype','get_img','readnum','createtime','isTop','status']
    list_filter = ['blogtype','isTop','status']
    search_fields = ['title','content','abstract']

    list_editable = ['isTop']


admin.site.register(Type,TypeAdmin)
admin.site.register(Tags,TagsAdmin)
admin.site.register(Blogs,BlogsAdmin)