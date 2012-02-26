from django.conf.urls.defaults import *
from AppSearch.views import search_page
import os

site_media = os.path.join(os.path.dirname(__file__), 'site_media')
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^App/', include('App.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^search/$', search_page),
    
    
    #Site Media
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media}),

)
