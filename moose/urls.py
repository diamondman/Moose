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
    (r'^$', TemplateView.as_view(template_name="home.html")),
    (r'^$',login),
    (r'^login/?$', login),
    url(r'test', 'moose.views.test1'),
    url(r'^get_deals', 'moose.views.get_deals'),
    url(r'^admin/', include(admin.site.urls)),
)
