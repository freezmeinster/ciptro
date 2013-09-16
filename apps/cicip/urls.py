from django.conf.urls import patterns, include, url

urlpatterns = patterns('cicip.views',
    url(r'^menyicip/$', 'nyicip', name='nyicip'),
    url(r'^mengenal/$', 'kenal', name='kenal'),
)