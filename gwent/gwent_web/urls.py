from django.conf.urls import include, url
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LoginView.as_view(), name='Login'),
    url(r'^logout/$', LogoutView.as_view()),
]