# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    #cid->auto created by django, pk
    name = models.CharField(max_length=30)


class Tag(models.Model):
    #tid->auto created by django, pk
    name = models.CharField(max_length=30)


class Article(models.Model):
    #aid->auto created by django, pk
    title = models.CharField(max_length=50)
    body = models.TextField()
    create_time = models.DateField()
    modified_time = models.DateField()
    excerpt = models.CharField(max_length=200, blank=True)

    author = models.ForeignKey(User)#edit by django
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)




