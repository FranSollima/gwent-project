from django.views.generic import RedirectView, FormView
from forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.
class LoginView(FormView):
	form_class = LoginForm
	#form_class = AuthenticationForm
	template_name = 'index.html'
	success_url= '/'

	def form_valid(self, form):
		url = self.request.META['HTTP_REFERER'].partition('?next=')[2]

 		usuario = form.cleaned_data['usuario']
 		password = form.cleaned_data['password']

		user = authenticate(username=usuario, password=password)
		if user is not None:
			if user.is_active:
				login(self.request, user)
				if url != '':
					return redirect(url)
				return redirect('/panel')
			self.request.session['mensaje_error'] = 'Usuario inactivo'
			return redirect('/')
		self.request.session['mensaje_error'] = 'Usuario y/o password incorrectos'
		return redirect('/')


class LogoutView(RedirectView):
	url='/'

	def get(self, request, *args, **kwargs):
		logout(request)
		return redirect(self.url)
