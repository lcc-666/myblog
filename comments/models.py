from django.db import models
from django.contrib.auth import get_user_model
from blogs.models import Blogs

User = get_user_model()


# Create your models here.

class Comments(models.Model):
    STATUS = (
        (1, '正常'),
        (2, '删除')
    )
    senduser = models.ForeignKey(User, verbose_name='评论人', on_delete=models.CASCADE, related_name='senduser')
    targetuser = models.ForeignKey(User, verbose_name='接受人', on_delete=models.CASCADE, related_name='targetuser', null=True, blank=True)
    blog = models.ForeignKey(Blogs, verbose_name='所属博客', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='内容')
    status = models.IntegerField(choices=STATUS, verbose_name='删除状态')
    createtime = models.DateTimeField(auto_now_add=True, verbose_name='新增时间')
    acceptparent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='上一级', null=True, blank=True)

    class Meta:
        verbose_name = '评论信息'
        verbose_name_plural = '评论信息'
        ordering = ['-createtime']

    def __str__(self):
        return self.content
