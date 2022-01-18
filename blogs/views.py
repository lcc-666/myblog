from django.shortcuts import render
from django.views import View
from blogs.models import *
from comments.models import Comments
# Create your views here.
class IndexView(View):
    def get(self,request):

        blogslist=Blogs.objects.filter(isDelete=False,isTop=True)
        data={
            'blogslist':blogslist
        }
        return render(request,'index.html',context=data)
from django.core.paginator import Paginator
class ArticleView(View):
    def get(self,request):
        type_id=request.GET.get('type')
        page=request.GET.get('page',1)
        if type_id is None:
            blogslist=Blogs.objects.all()
        else:
            blogslist=Blogs.objects.filter(blogtype_id=type_id)
        blogtypes=Type.objects.all()
        page_obj=Paginator(blogslist,5)
        page_data=page_obj.get_page(page)
        data_count=page_obj.count

        data = {
            'blogslist': page_data,
            'blogtypes': blogtypes,
            'data_count':data_count
        }
        return render(request,'article.html',context=data)

import markdown

class DetailView(View):
    def get(self,request,pk):
        blog=Blogs.objects.get(id=pk)
        blog.content = markdown.markdown(blog.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
        ])
        #comments=Comments.objects.filter(blog=blog)
        comments=Comments.objects.filter(blog_id=pk,status=1)
        data = {
            'blog': blog,
            'comments':comments

        }
        blog.readnum+=1
        blog.save()

        return render(request, 'detail.html',context=data)

class FilingView(View):
    def get(self,request,year,month):
        blogslist=Blogs.objects.filter(createtime__year=year,createtime__month=month)
        blogtypes = Type.objects.all()
        data = {
            'blogslist': blogslist,
            'blogtypes': blogtypes
        }
        return render(request,'article.html',context=data)


