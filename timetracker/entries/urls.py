from django.conf.urls import include, url

from entries import views


urlpatterns = [
    url(r'^entries/?$', views.entries, name='entries'),
    url(r'^clients/?$', views.clients, name='clients'),
    url(r'^clients/(?P<id>[^/]+)/?$', views.client_summary, name='client_summary'),
    url(r'^projects/?$', views.projects, name='projects'),
]
