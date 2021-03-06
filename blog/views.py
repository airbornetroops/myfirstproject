from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/base.html', locals())


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/detail.html', locals())
