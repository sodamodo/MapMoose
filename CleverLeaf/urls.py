from django.conf.urls import patterns, include, url
from django.contrib import admin
from Mapski import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.MainView.as_view(), name='base'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^map/', 'Mapski.views.map', name='map'),
    # url(r'^mapnik/render/tiles/', 'Mapski.views.map', name='tiles'),
    # url(r'^regprocess/', views.regprocess, name='regprocess'),
    url(r'^upload/', views.UploadView.as_view(), name='upload'),
    # url(r'^upload_process/', 'Mapski.views.upload_process', name='upshape'),
    url(r'^map/(?P<map_id>\d+)', 'Mapski.views.map', name='map'),
    url(r'^style/(?P<style_id>\d+)', 'Mapski.views.style', name='style'),
    url(r'^main/', views.MainView.as_view(), name='main'),
    url(r'^data/', views.data, name='data'),
    url(r'^save_style/', views.save_style, name='save_style'),

    url(r'^create_map/', views.CreateMap.as_view(), name='create_map'),




)
