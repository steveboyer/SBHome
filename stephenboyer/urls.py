from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import home.views

urlpatterns = [
    url(r'^$', home.views.index, name='index'),
    url(r'^db', home.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
