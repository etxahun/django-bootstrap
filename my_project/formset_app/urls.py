from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'formset_app.views.formset', name = 'formset'),
    url(r'^correct/$', 'formset_app.views.correct', name = 'correct'),
)

urlpatterns += staticfiles_urlpatterns()
