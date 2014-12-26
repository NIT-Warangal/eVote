from django.conf.urls import patterns, include, url
from django.contrib import admin
from vote import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'voting.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
)