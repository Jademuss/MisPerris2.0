from django.urls import path
from django.contrib import admin
from django.urls import include

from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('misperris.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,{
            'document_root':settings.MEDIA_ROOT,
        }),
    ]