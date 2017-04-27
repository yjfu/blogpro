from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/', view=views.findByCategory, name='category'),
    url(r'^article/', view=views.articlePage, name='article'),
    url(r'^tag/', view=views.findByTag, name='tag'),
    url(r'^keyWord/', view=views.findByKeyWord, name='keyWord'),
]