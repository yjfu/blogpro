# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render
from django.db import models
from comment import forms
from blog.models import Category, Article
from comment.views import getCommentList
import codecs
import markdown


def findByTag(request):
    tags = request.GET
    return render(request, 'linkt.html', context={'content': str(tags)})


def findByKeyWord(request):
    keyWord = request.GET
    return render(request, 'linkt.html', context={'content': str(keyWord)})


def articlePage(request):
    path = request.path
    articleId = int(path.split(r'/')[-1]) - 1
    article = [getTestarticleList()[articleId]]

    catagoryList = getTestCategoryList()
    tagList = getTestTagList()

    return render(request, 'article-body.html', context={'title': "X's Blog",
                                                         'category_list': catagoryList,
                                                         'tag_list': tagList,
                                                         'article_list': article,
                                                         'form': forms.CommentForm(),
                                                         'comment_list': getCommentList(article_pk=(articleId+1))
                                                         })


def findByCategory(request):
    path = request.path
    category = path.split(r'/')[-1]

    return render(request, 'linkt.html', context={'content': category})


def index(request):
    catagoryList = getTestCategoryList()
    tagList = getTestTagList()
    articleList = getTestarticleList()
    return render(request, 'index.html', context={'title': "X's Blog",
                                                  'category_list': catagoryList,
                                                  'tag_list': tagList,
                                                  'article_list': articleList})


def getTestCategoryList():
    C = type(str('C'), (), {})
    category1 = C()
    category1.name = '类别1'
    category1.link = '/category/' + category1.name
    category2 = C()
    category2.name = '类别2'
    category2.link = '/category/' + category2.name

    category_list = [category1, category2]
    return category_list


def getTestTagList():
    T = type(str('T'), (), {})
    tag1 = T()
    tag1.id = 't1'
    tag1.name = '标签1'
    tag2 = T()
    tag2.id = 't2'
    tag2.name = '标签2'

    tag_list = [tag1, tag2]
    return tag_list


def getTestarticleList():
    # A = type(str('A'), (), {})
    # article1 = A()
    # article1.articleId = 1
    # article1.title = '第一篇文章的标题'
    # article1.author = 'author'
    # article1.category = 'class1'
    # article1.create_date = '2017年 四月25日'
    # article1.excerpt = '这是一篇示例文章,这里是他的简介,' \
    #                    '可以再长一点再长一点再长一点可以再长一点再' \
    #                    '长一点再长一点可以再长一点再长一点再长一点' \
    #                    '可以再长一点再长一点再长一点可以再长一点再' \
    #                    '长一点再长一点长一点再长一点长一点再长一点长一点' \
    #                    '再长一点长一点再长一点长一点再长一点长一点再长一点' \
    #                    '长一点再长一点长一点再长一点长一点再长一点长一点再' \
    #                    '长一点长一点再长一点长一点再长一点长一点再长一点'
    # article1.link = '/article/' + str(article1.articleId)
    # file = codecs.open('blog/test.md', 'r', encoding='utf-8')
    # s = file.read()
    #
    # s = markdown.markdown(s, extensions=[
    #     'markdown.extensions.extra',
    #     'markdown.extensions.codehilite',
    #     'markdown.extensions.toc',
    # ])
    # article1.body = s
    # article2 = A()
    # article2.articleId = 2
    # article2.title = '第二篇文章的标题'
    # article2.author = 'author'
    # article2.category = 'class1'
    # article2.create_date = '2017年 四月25日'
    # article2.excerpt = '这是一篇示例文章,这里是他的简介'
    # article2.link = '/article/' + str(article2.articleId)
    # article_list = [article1, article2]
    # article2.body = '内容'
    articleList = Article.objects.all()
    for article in articleList:
        article.link = '/article/' + str(article.pk)
    article.body = markdown.markdown(article.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    return articleList

# def addCategory(categoryName):
#
