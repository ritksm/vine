from django.conf.urls import patterns, include, url
from d1.views import *
from django.conf.urls import *
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^hi/$', hi),
    #('^$', hi),
    ('^time/$', time),
    ('^comment/$', comment_board),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^write/(\w{1,40})$', comment_board),
    (r'^test/', test_func),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #{'document_root': settings.STATIC_ROOT}),
    # Examples:
    # url(r'^$', 'd1.views.home', name='home'),
    # url(r'^d1/', include('d1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('',
    url(r'^articles/comments/', include('django.contrib.comments.urls')),
)

urlpatterns += patterns('',
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
)


from functools import wraps
from django.conf import settings
from django.contrib.staticfiles.views import serve as serve_static
from django.conf.urls import patterns, url


if settings.DEBUG:

    def custom_headers(view_func):

        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            response = view_func(request, *args, **kwargs)
            response['Access-Control-Allow-Origin'] = '*'
            response['Custom-header'] = 'Awesome'
            response['Another-header'] = 'Bad ass'
            return response

        return wrapper

    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', custom_headers(serve_static)),
    )