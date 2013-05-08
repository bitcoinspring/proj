from django.conf.urls import patterns, include, url
import home
import validate

urlpatterns = patterns('',
    url(r'^$', 'home.views.home', name='home'),
    url(r'^order/', 'home.views.order', name='order'),
    url(r'^validate/', 'validate.views.recv', name='recv'), 

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
