from django.conf.urls import url

from . import views

app_name = 'comment'
urlpatterns = [
    url(r'^comment/article/(?P<article_pk>[0-9]+)/$', views.articleComment, name='articleComment'),
]