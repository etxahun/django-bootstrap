from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'markup_app.views.index', name = 'index'),
    url(r'^typography/$', 'markup_app.views.typography', name = 'typography'),
    url(r'^emphasis/$', 'markup_app.views.emphasis', name = 'emphasis'),
)

urlpatterns += staticfiles_urlpatterns()
