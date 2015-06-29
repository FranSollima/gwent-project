from django.views.generic import TemplateView

# Create your views here.
class PanelView(TemplateView):
	template_name = 'panel.html'