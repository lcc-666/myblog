from django.contrib import admin
from comments.models import Comments
# Register your models here.

class CommtnesAdmin(admin.ModelAdmin):
    list_display = ['senduser','acceptparent','targetuser','content','createtime']

admin.site.register(Comments,CommtnesAdmin)
