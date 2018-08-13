# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from blog import models
#admin.site.register(models.Blog)

# Register your models here.
@admin.register(models.BlogType)
class BolgTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')
@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','blog_type','author','get_read_num','created_time','last_updated_time')
