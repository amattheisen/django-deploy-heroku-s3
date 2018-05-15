from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views
import blog.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    # Hello App
    url(r'^$', hello.views.index, name='hello-index'),
    url(r'^db', hello.views.db, name='hello-db'),
    # Blog App
    url(r'^blog/?$', blog.views.index, name='blog_index'),
    url(r'^blog/(?P<slug>[\w\-]+)/$', blog.views.post, name='blog_post'),
    # Admin App
    path('admin/', admin.site.urls),
]
