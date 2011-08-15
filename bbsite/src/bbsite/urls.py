from django.conf.urls.defaults import *
from django.contrib.admin.views.decorators import staff_member_required
from blog.views import *
from django.contrib import admin
from bbsite.blog.views import show_published_blog
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^blogs/drafts/$', staff_member_required(list_draft_blogs)),
    (r'^blogs/', list_published_blogs),
    (r'^blog/title/(?P<blog_title>[-\w]+)/$', show_published_blog),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)