from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('nginxpurge.views',
    # Examples:
    # url(r'^$', 'nginxpurge.views.home', name='home'),
    # url(r'^nginxpurge/', include('nginxpurge.foo.urls')),
    url(r'^$', 'index'),
    url(r'^clean/$', 'clean'),
    url(r'^results/$', 'results'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
