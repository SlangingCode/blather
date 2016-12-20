"""blather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blat import views as blat_views
from rockmysocks import views as rmo_views

urlpatterns = [
    # Blat
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', blat_views.IndexView.as_view(), name='homepage'),
    url(r'^(?P<pk>[0-9]+)/$', blat_views.DetailView.as_view(), name='detail'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^my/$', blat_views.MyView.as_view(), name='myview'),
    url(r'^create/$', blat_views.NewBlatView.as_view(), name='newblat'),
    url(r'^(?P<pk>[0-9]+)/edit/$', blat_views.EditBlatView.as_view(), name='editblat'),

    # Rock Me Out
    url(r'^rockmysocks/$', rmo_views.home, name='rms_homepage'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
