from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'cicip.views.home', name='home'),
    url(r'^cicip/', include('cicip.urls')),
    url(r'^login/$', 'cicip.views.login_page', name='login'),
    url(r'^logout$', 'cicip.views.logout_page', name='logout'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
