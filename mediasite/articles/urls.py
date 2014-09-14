from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


#urlpatterns = patterns('haystack.views',
#    url(r'^$', FacetedSearchView(form_class=FacetedSearchForm, searchqueryset=sqs), name='haystack_search'),
#)
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'articles.views.main',name='home'),
    url(r'^alogin/$', 'articles.views.login',name='login'),
    url(r'^logout/$', 'articles.views.logout',name='logout'),
    url(r'^write/$', 'articles.views.upload_view',name='uploadview'),
    url(r'^listarticle/$', 'articles.views.file_view',name='fileview'),
    url(r'^profile/$', 'articles.views.authors'),
    url(r'^author_add/$', 'articles.views.author_add'),
    url(r'^author_edit/$','articles.views.author_edit'),
    url(r'^search/', 'articles.views.search_posts'),
    url(r'^category/(?P<cat_id>\d+)/$', 'articles.views.category_detail'),
    url(r'^article/(?P<article_id>\d+)/$', 'articles.views.article_detail'),

   )


