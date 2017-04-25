"""blogpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^$', view=views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^category/', view=views.findByCategory, name='category'),
    url(r'^article/', view=views.articlePage, name='article'),
    url(r'^tag/', view=views.findByTag, name='tag'),
    url(r'^keyWord/', view=views.findByKeyWord, name='keyWord')
]
