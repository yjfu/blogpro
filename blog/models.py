# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    #cid->auto created by django, pk
    name = models.CharField(max_length=30)

    def __str__(self):
        print(self.name)
        return self.name[:20].encode('utf8')
        #return self.name


class Tag(models.Model):
    #tid->auto created by django, pk
    name = models.CharField(max_length=30)

    def __str__(self):

        return self.name[:20].encode('utf8')
        #return self.name


class Article(models.Model):
    #aid->auto created by django, pk
    title = models.CharField(max_length=50)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    excerpt = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=20, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title[:20].encode('utf8')
        #return self.title






