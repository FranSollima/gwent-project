from django.views.generic import TemplateView
from gwent_web.mixins import LoginRequiredMixin

# Create your views here.
class PanelView(LoginRequiredMixin, TemplateView):
	template_name = 'panel.html'