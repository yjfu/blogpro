# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from comment import forms
from django.shortcuts import render
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
    pk = int(path.split(r'/')[-1])-1
    al = [getTestarticleList()[pk]]
    cl = getTestCategoryList()
    tl = getTestTagList()

    return render(request, 'article-body.html', context={'title': "X's Blog",
                                                  'category_list': cl,
                                                  'tag_list': tl,
                                                  'article_list': al,
                                                   'form': forms.CommentForm(),
                                                         })


def findByCategory(request):
    path = request.path
    category = path.split(r'/')[-1]

    return render(request, 'linkt.html', context={'content': category})



def index(request):
    cl = getTestCategoryList()
    tl = getTestTagList()
    al = getTestarticleList()
    return render(request, 'index.html', context={'title': "X's Blog",
                                                  'category_list': cl,
                                                  'tag_list': tl,
                                                  'article_list': al})


def getTestCategoryList():
    C = type(str('C'), (), {})
    category1 = C()
    category1.name = '类别1'
    category1.link = '/category/'+category1.name
    category2 = C()
    category2.name = '类别2'
    category2.link = '/category/'+category2.name

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
    A = type(str('A'), (), {})
    article1 = A()
    article1.pk = 1
    article1.title = '第一篇文章的标题' 
    article1.author = 'author'
    article1.category = 'class1'
    article1.create_date = '2017年 四月25日'
    article1.excerpt = '这是一篇示例文章,这里是他的简介,' \
                       '可以再长一点再长一点再长一点可以再长一点再' \
                       '长一点再长一点可以再长一点再长一点再长一点' \
                       '可以再长一点再长一点再长一点可以再长一点再' \
                       '长一点再长一点长一点再长一点长一点再长一点长一点' \
                       '再长一点长一点再长一点长一点再长一点长一点再长一点' \
                       '长一点再长一点长一点再长一点长一点再长一点长一点再' \
                       '长一点长一点再长一点长一点再长一点长一点再长一点'
    article1.link = '/article/'+str(article1.pk)
    file = codecs.open('blog/test.md', 'r', encoding='utf-8')
    s = file.read()

    s = markdown.markdown(s, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    article1.body = s
    article2 = A()
    article2.pk = 2
    article2.title = '第二篇文章的标题'
    article2.author = 'author'
    article2.category = 'class1'
    article2.create_date = '2017年 四月25日'
    article2.excerpt = '这是一篇示例文章,这里是他的简介'
    article2.link = '/article/'+str(article2.pk)
    article_list = [article1, article2]
    article2.body = '内容'
    return article_list