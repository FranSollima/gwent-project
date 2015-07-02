from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from .views import *

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LoginView.as_view(), name='Login'),
    url(r'^accounts/login/$', LoginView.as_view(), name='Login'),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^register', CreateView.as_view(template_name='register.html',form_class=UserCreationForm,success_url='/'))

]