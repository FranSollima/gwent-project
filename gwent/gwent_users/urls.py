from django.conf.urls import include, url
from .views import *

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^panel/$', PanelView.as_view(), name='Panel'),
]