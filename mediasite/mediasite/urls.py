from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mediasite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^', 'articles.views.main'),
    url(r'^', include('articles.urls')),
    url(r'^admin/', include(admin.site.urls)),
 )

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_URL}),
)

# this code is append for static file
urlpatterns += patterns('',
    url(r'^static/articles/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)
