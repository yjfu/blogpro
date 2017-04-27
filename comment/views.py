# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def articleComment(request,article_pk):
    comment = request.POST
    return render(request, 'linkt.html', context={'content': str(comment)+"PK"+article_pk})
