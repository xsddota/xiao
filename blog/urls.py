from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.blog_list,name='blog_list'),
    url(r'^(?P<blog_pk>[0-9]+)/$',views.blog_detail,name='blog_detail'),
    url(r'^type/(?P<blogs_with_type>[0-9]+)/$',views.blogs_with_type,name='blogs_with_type'),
    url(r'^date/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$',views.blogs_with_date,name='blogs_with_date'),
]