from django.conf.urls import include, url
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url('^accounts/', include('registration.urls')),
]