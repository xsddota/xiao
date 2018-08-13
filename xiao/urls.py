"""xiao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# from blog.views import article_detail
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'blog/<int:atricle_id>$',article_detail,name='article_detail'),
    # url(r'^add/$',views.add,name='add'),
    # url(r'^add2/(\d+)/(\d+)/$',views.add2,name='add2'),
    url(r'^$', views.home,name='home'),
    url(r'^ckediotr/', include('ckeditor_uploader.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^comment/', include('comment.urls')),
    url(r'^likes/', include('likes.urls')),
    url(r'^user/', include('user.urls')),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)