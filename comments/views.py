from django.shortcuts import get_object_or_404, redirect
from django.views import View
from comments.models import Comments
from blogs.models import Blogs
from django.shortcuts import render
# Create your views here.

class CreateVIem(View):
    def post(self, request, pk):
        blog = get_object_or_404(Blogs,id=pk)
        if request.session['status']!= 1:
            return render(request, 'login.html', context={'data': '请先登录后在评论' })
        targetuser = request.POST.get('targetuser')
        acceptparent = request.POST.get('acceptparent')
        senduser = request.user
        content = request.POST.get('content')
        com=Comments()
        com.blog=blog
        if acceptparent is not None:
            com.acceptparent_id=acceptparent
            com.targetuser_idr=targetuser
        com.senduser=senduser
        com.content=content
        com.status=1
        com.save()
        return redirect(blog.get_detail_url())
