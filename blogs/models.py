
from django.contrib.auth import get_user_model
from django.db import models

User=get_user_model()

# Create your models here.


class Type(models.Model):
    name=models.CharField(max_length=20,verbose_name='标签名称')
    describe=models.CharField(max_length=255,verbose_name='描述信息')

    class Meta:
        verbose_name='分类信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class Tags(models.Model):
    name=models.CharField(max_length=20,verbose_name='标签名称')
    describe=models.CharField(max_length=255,verbose_name='描述信息')
    class Meta:
        verbose_name='标签信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class Blogs(models.Model):
    STATUS=(
        (1,'公开'),
        (2,'私密')
    )
    title=models.CharField(max_length=100,verbose_name='标题')
    abstract=models.CharField(max_length=255,verbose_name='摘要')
    content=models.TextField(verbose_name='内容')
    img=models.ImageField(upload_to='blogs/%Y/%n?/',verbose_name='封面图片')
    readum=models.IntegerField(default=0,verbose_name='阅读量')
    commentnum=models.IntegerField(default=0,verbose_name='评论量')
    status=models.IntegerField(choices=STATUS,verbose_name='状态')
    isDelete=models.BooleanField(default=False,verbose_name='是否删除')
    isTop=models.BooleanField(default=False,verbose_name='是否置顶')
    createtime=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    updatetime=models.DateTimeField(auto_now_add=True,verbose_name='修改时间')
    blogtype=models.ForeignKey('type',on_delete=models.PROTECT,verbose_name='所属分类')
    user=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name='作者')
    tags=models.ManyToManyField('tags',related_name='tags',verbose_name='标签')

    class Meta:
        verbose_name='博文信息'
        verbose_name_plural=verbose_name
        ordering=('-createtime',)

    def __str__(self):
        return self.title