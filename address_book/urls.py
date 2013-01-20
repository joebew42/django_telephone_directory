from django.conf.urls import patterns, include, url

urlpatterns = patterns('address_book.views',
    url(r'^$', 'index'),
    url(r'^search/$', 'search'),
    url(r'^detail/(?P<entry_id>\d+)/$', 'detail'),
    url(r'^edit/$', 'edit'),
    url(r'^edit/(?P<entry_id>\d+)/$', 'edit',
        name="address_book.views.edit_existing"),
)
