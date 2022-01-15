from django.contrib import admin
from .models import Type,Tags,Blogs

# Register your models here.


class TypeAdmin(admin.ModelAdmin):
    list_display = ['name','describe']

class TagsAdmin(admin.ModelAdmin):
    list_display = ['name','describe']

class BlogsAdmin(admin.ModelAdmin):
    list_display = ['title', 'abstract']


admin.site.register(Type,TypeAdmin)

admin.site.register(Tags,TagsAdmin)

admin.site.register(Blogs,BlogsAdmin)
