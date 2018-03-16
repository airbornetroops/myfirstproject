from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    body = models.TextField(verbose_name='内容')
    excerpt = models.CharField(max_length=200, blank=True, null=True, verbose_name='摘要')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')

    # 定义表关联关系
    category = models.ForeignKey('Category', verbose_name='类别')
    tag = models.ManyToManyField('Tag', blank=True, verbose_name='标签')
    author = models.ForeignKey(User, verbose_name='作者')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = '帖子'
        verbose_name = '帖子'