# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from blog.models import Article


# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, null=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.PROTECT)

    def __str__(self):
        return self.title[:20].encode('utf8')
