from django.conf.urls import patterns, include, url
from django.contrib import admin
from vote import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'voting.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.loginpage, name='login'),
    url(r'^logout/', views.logoutpage, name='logout'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^signup/', views.signuppage, name='signup'),
    url(r'^candidates/', views.candidates, name='candidates'),
    url(r'^thanks/', views.thankyou, name='thanks')
)