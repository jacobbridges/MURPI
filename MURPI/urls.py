"""MUI URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

from murpi_core import views as core_views


urlpatterns = [
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^player/@(?P<username>[A-Za-z0-9_]+)/$', core_views.retrieve_player, name="player"),
    url(r'^register/$', core_views.show_create_player, name="show_register"),
    url(r'^register_player/$', core_views.create_player, name="register"),
    url(r'^login/$', core_views.show_login, name="show_login"),
    url(r'^logout/$', core_views.logout, name="logout"),
    url(r'^validate_login/$', core_views.login, name="login")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
