from django.shortcuts import render
from django.views import View
from blogs.models import *
# Create your views here.
class IndexView(View):
    def get(self,request):
        #blogslist=Blogs.objects.all()
        blogslist=Blogs.objects.filter(isDelete=False,isTop=True)
        data={
            'blogslist':blogslist
        }
        return render(request,'index.html',context=data)

class ArticleView(View):
    def get(self,request):
        # #blogslist=Blogs.objects.all()
        # blogslist=Blogs.objects.filter(isDelete=False,isTop=True)
        # data={
        #     'blogslist':blogslist
        # }
        return render(request,'article.html',)