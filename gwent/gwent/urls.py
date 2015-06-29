from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('gwent_web.urls')),
    url(r'^', include('gwent_users.urls')),
]