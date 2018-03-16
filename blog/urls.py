from django.conf.urls import url
from .views import index, detail

app_name = 'blog'

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', detail, name='detail')
]