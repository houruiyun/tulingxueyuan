import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tulingxueyuan.settings")

django.setup()

from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as tv
urlpatterns = [
    # Examples:
    # url(r'^$', 'tulingxueyuan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^normalmap/', tv.do_normalmap),
]
