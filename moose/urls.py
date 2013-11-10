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
    url(r'^user/(\d{4})/(?P<name>\w+)$', 'moose.views.test1'),
    (r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'test', 'moose.views.test1'),
    url(r'^get_deals', 'moose.views.get_deals'),
    url(r'^admin/', include(admin.site.urls)),
)
