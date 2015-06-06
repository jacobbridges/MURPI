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
    url(r'^players/$',                                          core_views.retrieve_players,            name="players"),
    url(r'^player/@(?P<username>[A-Za-z0-9_]+)/$',              core_views.retrieve_player,             name="player"),
    url(r'^player/@(?P<username>[A-Za-z0-9_]+)/characters/$',   core_views.retrieve_player_characters,  name="player_characters"),
    url(r'^universe/(?P<universe_id>[0-9]+)/$',                 core_views.retrieve_universe,           name="universe"),
    url(r'^universes/$',                                        core_views.retrieve_universes,          name="universes"),
    url(r'^universes/create/$',                                 core_views.create_universe,             name="create_universe"),
    url(r'^universe/(?P<universe_id>[0-9]+)/worlds/$',          core_views.retrieve_worlds,             name="worlds"),
    url(r'^universe/(?P<universe_id>[0-9]+)/worlds/create/$',   core_views.create_world,                name="create_world"),
    url(r'^world/(?P<world_id>[0-9]+)/$',                       core_views.retrieve_world,              name="world"),
    url(r'^world/(?P<world_id>[0-9]+)/places/$',                core_views.retrieve_places,             name="places"),
    url(r'^world/(?P<world_id>[0-9]+)/places/create/$',         core_views.create_place,                name="create_place"),
    url(r'^place/(?P<place_id>[0-9]+)/$',                       core_views.retrieve_place,              name="place"),
    url(r'^register/$',                                         core_views.register,                    name="register"),
    url(r'^login/$',                                            core_views.login,                       name="login"),
    url(r'^logout/$',                                           core_views.logout,                      name="logout"),
    url(r'^rps/create/$',                                       core_views.create_rp,                   name="create_rp"),
    url(r'^rp/(?P<rp_id>[0-9]+)/$',                             core_views.retrieve_rp,                 name="rp"),
    url(r'^rp/(?P<rp_id>[0-9]+)/scenes/$',                      core_views.retrieve_scenes_rp_view,     name="scenes_rp_view"),
    url(r'^rp/(?P<rp_id>[0-9]+)/scenes/create/$',               core_views.create_scene_rp_view,        name="create_scene_rp_view"),
    url(r'^scene/(?P<scene_id>[0-9]+)/$',                       core_views.retrieve_scene,              name="scene")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
