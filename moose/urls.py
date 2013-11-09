from django.conf.urls import patterns, include, url
from moose.views import *
from django.contrib import admin
admin.autodiscover()

from moose.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moose.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^&', 'login'),url(r'test', test1),
    url(r'^get_deals', 'get_deals'),
    url(r'^admin/', include(admin.site.urls)),
)
