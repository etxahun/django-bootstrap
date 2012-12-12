from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'formset_app.views.formset', name = 'formset'),
    url(r'^added/$', 'formset_app.views.added', name = 'added'),
)

urlpatterns += staticfiles_urlpatterns()
