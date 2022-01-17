from django.shortcuts import render
from django.views import View
from blogs.models import *
# Create your views here.
class IndexView(View):
    def get(self,request):

        blogslist=Blogs.objects.filter(isDelete=False,isTop=True)
        data={
            'blogslist':blogslist
        }
        return render(request,'index.html',context=data)

class ArticleView(View):
    def get(self,request):
        type_id=request.GET.get('type')
        if type_id is None:
            blogslist=Blogs.objects.all()
        else:
            blogslist=Blogs.objects.filter(blogtype_id=type_id)
        blogtypes=Type.objects.all()
        data={
            'blogslist':blogslist,
            'blogtypes':blogtypes
        }
        return render(request,'article.html',context=data)

class DetailView(View):
    def get(self,request,pk):
        print(pk)
        blogs=Blogs.objects.get(id=pk)
        data = {
            'blog': blogs
        }
        print(blogs)

        return render(request, 'detail.html',context=data)
