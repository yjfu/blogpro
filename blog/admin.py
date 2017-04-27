# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from models import Article, Category, Tag

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
