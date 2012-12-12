from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'contact_app.views.contact', name = 'contact'),
    url(r'^correct/$', 'contact_app.views.correct', name = 'correct'),
)

urlpatterns += staticfiles_urlpatterns()
