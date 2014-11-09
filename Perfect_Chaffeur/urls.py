from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Services.views.home'),
    url(r'^login/','Services.views.login'),
    url(r'^test_login/','Services.views.test_login'),
    url(r'^form/','Services.views.form'),
    url(r'^check_fligths/','Services.views.check_fligths'),
    url(r'^fligth_search/','Services.views.fligth_search'),
    url(r'^sign_up/','Services.views.sign_up'),
    url(r'^sign_up_user/','Services.views.sign_up_user'), 
    #url(r'^frames/','Services.views.frames'), 
    #url(r'^creditcard/','Services.views.creditcard'),                 
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
