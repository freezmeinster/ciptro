from django.conf.urls import patterns, include, url

urlpatterns = patterns('cicip.views',
    url(r'^tambah/(?P<version_id>\d+)/$', 'tambah_cicip', name="tambah_cicip"),
    url(r'^nonton/(?P<id>\d+)/$', 'nonton_cicip', name="nonton_cicip"),
    url(r'^hapus/(?P<id>\d+)/$', 'hapus_cicip', name="hapus_cicip"),
    url(r'^menyicip/$', 'nyicip', name='nyicip'),
    url(r'^mengenal/$', 'kenal', name='kenal'),
)