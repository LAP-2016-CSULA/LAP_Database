"""
Definition of urls for djangoDatabase.
"""

from datetime import datetime
from django.conf.urls import patterns, url, include
from phenology.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^phenology/', include('phenology.urls')),
    # Examples:
    url(r'^$', 'phenology.views.home', name='home'),
    url(r'^contact$', 'phenology.views.contact', name='contact'),
    url(r'^about', 'phenology.views.about', name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'phenology/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
)
