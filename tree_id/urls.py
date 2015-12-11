from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'tree_id.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^admin/', include(admin.site.urls)),
#
# )

urlpatterns = [
    url(r'^trees/', include('trees.urls', namespace='trees')),
    url(r'^admin/', include(admin.site.urls)),
]
