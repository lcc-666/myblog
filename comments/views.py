from django.shortcuts import get_object_or_404, redirect
from django.views import View
from comments.models import Comments
from blogs.models import Blogs
from django.urls import reverse

# Create your views here.

class CreateVIem(View):
    def post(self, request, pk):
        blog = get_object_or_404(Blogs,id=pk)
        targetuser = request.POST.get('targetuser')
        acceptparent = request.POST.get('acceptparent')
        senduser = request.user
        content = request.POST.get('content')
        # data = {
        #     'blog': blog,
        #     'targetuser': targetuser,
        #     'acceptparent': acceptparent,
        #     'senduser': senduser,
        #     'content': content,
        #     'status': 1
        # }
        # Comments.objects.create(**data)

        com=Comments()
        com.blog=blog
        if acceptparent is not None:
            com.acceptparent=acceptparent
            com.targetuser=targetuser
        com.senduser=senduser
        com.content=content
        com.status=1
        com.save()
    #     < form
    #
    #     class ="layui-form blog-editor" method="post" action="{% url 'comments:create' blog.id %}" >
    #
    #     { % csrf_token %}
    #     < input
    #     type = "hidden"
    #     name = "articleid"
    #     id = "articleid"
    #     value = "@Model.ID" >
    #     < div
    #
    #     class ="layui-form-item" >
    #
    #     < textarea
    #     name = "content"
    #     lay - verify = "content"
    #     id = "remarkEditor"
    #     placeholder = "请输入内容"
    #
    #     class ="layui-textarea layui-hide" > < / textarea >
    #
    # < / div >
    # < di

        return redirect(blog.get_detail_url())
        #return redirect(reverse)
