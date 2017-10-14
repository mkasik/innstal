from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import innstal.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', include('django.contrib.auth.urls')),
    url(r'^$', innstal.views.index, name='index'),
    url(r'^login', innstal.views.login, name='login'),
    url(r'^register_warrantly', innstal.views.register_warrantly, name='login'),
    url(r'^pricing', innstal.views.pricing, name='pricing'),
    url(r'^service', innstal.views.service, name='service'),
    url(r'^about', innstal.views.about, name='about'),
    url(r'^contact', innstal.views.contact, name='contact'),
    url(r'^search_result', innstal.views.search_result, name='search_result'),
    url(r'^signup', innstal.views.SignUp),
    # url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
