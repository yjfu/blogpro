# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from comment.models import Comment
from blog.models import Article
from comment.forms import CommentForm


# Create your views here.

def articleComment(request, article_pk):
    print(article_pk)
    # post = Article.objects.get(pk=article_pk)
    post = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = post
            comment.save()
            return redirect('/article/' + str(post.pk))
    return render(request, 'linkt.html', context={'content': str(post) + "PK" + article_pk})


def getCommentList(article_pk):
    return Comment.objects.filter(article__pk__exact=article_pk)
