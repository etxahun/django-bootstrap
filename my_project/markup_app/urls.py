from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'markup_app.views.index', name = 'index'),
    url(r'^typography/$', 'markup_app.views.typography', name = 'typography'),
)

urlpatterns += staticfiles_urlpatterns()
