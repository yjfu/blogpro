# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render
from django.db import models, connection, transaction
from comment import forms
from blog.models import Category, Article, Tag
from comment.views import getCommentList
import codecs
import markdown


def findByTag(request):
    path = request.GET
    a = 0
    tags = list(path.keys())

    cursor = connection.cursor()
    sql = 'select article_id from blog_article_tags where '

    for tag in tags:
        a += 1
        if tag == tags[-1]:
            sql += ' tag_id = '
            sql += tag
        else:
            sql += ' tag_id = '
            sql += tag[0]
            sql += ' OR '
    sql += ' group by article_id having count(article_id)='
    sql += str(tags.__len__())
    sql += ';'

    if a == 0:
        return index(request)
    categoryList = getCategoryList()
    tagList = getTagList()

    cursor.execute(sql)
    articleIdList = cursor.fetchall()


    articleList = []
    for article_id in articleIdList:
        tmp = article_id[0]
        articleList.append(Article.objects.get(id=tmp))

    for article in articleList:
        article.link = '/article/' + str(article.pk)
        s = markdown.markdown(article.body, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        article.body = s

    return render(request, 'index.html', context={'title': "X's Blog",
                                                  'category_list': categoryList,
                                                  'tag_list': tagList,
                                                  'article_list': articleList})


def findByKeyWord(request):
    keyWord = request.GET['keyWord']
    if keyWord == "":
        return index(request)
    categoryList = getCategoryList()
    tagList = getTagList()
    articleList = []
    ids = {}

    try:
        articleList_body = Article.objects.filter(body__contains=keyWord)
    except Article.DoesNotExist:
        try:
            articleList_title = Article.objects.filter(title__contains=keyWord)
        except Article.DoesNotExist:
            pass
    try:
        articleList_title = Article.objects.filter(title__contains=keyWord)
    except Article.DoesNotExist:
        pass

    for article in articleList_body:
        article.link = '/article/' + str(article.pk)
        articleList.append(article)
        ids[article.pk] = 1
    for article in articleList_title:
        if ids[article.pk] != 1:
            article.link = '/article/' + str(article.pk)
            articleList.append(article)

    return render(request, 'index.html', context={'title': "X's Blog",
                                                  'category_list': categoryList,
                                                  'tag_list': tagList,
                                                  'article_list': articleList})


def articlePage(request):
    path = request.path
    articleId = int(path.split(r'/')[-1]) - 1
    article = [getArticleList()[articleId]]
    catagoryList = getCategoryList()
    tagList = getTagList()

    s = markdown.markdown(article[0].body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    article[0].body = s

    return render(request, 'article-body.html', context={'title': "X's Blog",
                                                         'category_list': catagoryList,
                                                         'tag_list': tagList,
                                                         'article_list': article,
                                                         'form': forms.CommentForm(),
                                                         'comment_list': getCommentList(article_pk=(articleId + 1))
                                                         })


def findByCategory(request):
    path = request.path
    category_pk = Category.objects.get(name=path.split(r'/')[-1]).pk
    catagoryList = getCategoryList()
    tagList = getTagList()

    articleList = Article.objects.filter(category__pk__exact=category_pk)

    for article in articleList:
        article.link = '/article/' + str(article.pk)

    return render(request, 'index.html', context={'title': "X's Blog",
                                                  'category_list': catagoryList,
                                                  'tag_list': tagList,
                                                  'article_list': articleList})

    # return render(request, 'linkt.html', context={'content': category})


def index(request):
    catagoryList = getCategoryList()
    tagList = getTagList()
    articleList = getArticleList()
    return render(request, 'index.html', context={'title': "X's Blog",
                                                  'category_list': catagoryList,
                                                  'tag_list': tagList,
                                                  'article_list': articleList})


def getCategoryList():
    category_list = Category.objects.all()
    for category in category_list:
        category.link = '/category/' + category.name
    return category_list


def getTagList():
    return Tag.objects.all()


def getArticleList():
    articleList = Article.objects.all()
    for article in articleList:
        article.link = '/article/' + str(article.pk)
    return articleList


