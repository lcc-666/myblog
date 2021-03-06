# Generated by Django 3.2.9 on 2022-01-17 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogs', '0005_alter_blogs_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('status', models.IntegerField(choices=[(1, '正常'), (2, '删除')], verbose_name='删除状态')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='新增时间')),
                ('acceptparent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.comments', verbose_name='上一级')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.blogs', verbose_name='所属博客')),
                ('senduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senduser', to=settings.AUTH_USER_MODEL, verbose_name='评论人')),
                ('targetuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targetuser', to=settings.AUTH_USER_MODEL, verbose_name='接受人')),
            ],
            options={
                'verbose_name': '评论信息',
                'verbose_name_plural': '评论信息',
                'ordering': ['-createtime'],
            },
        ),
    ]
