from django.conf.urls import patterns, include, url
from moose.views import *
from django.contrib import admin
admin.autodiscover()

from django.views.generic import TemplateView

from moose.views import *

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'moose.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',login),
    url(r'^login/?$', login),
    url(r'new_user/?$', newUser),
    url(r'^get_deals/?$', deals),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^favorites/?$', favorites),
    url(r'^fav.json/?$', fav_json),
    url(r'^get_deals.json$', get_deals_json),
    url(r'^demo/?$', demo),
    url(r'^setasfavorite/(\d+)/(\w+)/?$', set_favorite),
    url(r'^getasfavorite/(\d+)/?$', get_favorite),
)
