from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'my_project.views.home', name = 'home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # contact_app url
    url(r'^contact/', include('contact_app.urls')),

    # formset_app url
    url(r'^formset/', include('formset_app.urls')),

    # markup_app url
    url(r'^markup/', include('markup_app.urls')),

    # Just for development purposes, should be served in another way in production
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += staticfiles_urlpatterns()
