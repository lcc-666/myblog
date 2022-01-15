from django.contrib import admin
from blogs.models import *
# from blogs.models import Type
# Register your models here.
# 注册模型，让后台管理系统可以进行管理

# 修改后台管理系统的名称和标题
admin.site.site_header = "个人博客管理系统"
admin.site.site_title = "个人博客管理系统"

# 扩展相关配置
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name','describe']


class TagsAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe']

class BlogsAdmin(admin.ModelAdmin):
    # 配置表格所展示哪些列的数据
    list_display = ['title','abstract','blogtype','get_img','readnum','createtime','isTop','status']
    # 配置列表数据展示的过滤功能：外键??、布尔类型字段、类似枚举类型
    list_filter = ['blogtype','isTop','status']
    # 模糊查询
    search_fields = ['title','content','abstract']
    # 配置表格列表中可以修改的字段
    list_editable = ['isTop']
    # 指定排序字段
    # ordering =

admin.site.register(Type,TypeAdmin)
admin.site.register(Tags,TagsAdmin)
admin.site.register(Blogs,BlogsAdmin)