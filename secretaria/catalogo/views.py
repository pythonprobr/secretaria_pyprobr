from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView

from .forms import EmailForm

# Create your views here.
home_page = None

def home_page(request):
    return HttpResponse('<html><title>Python.pro.br: Catálogo de cursos</title></html>')


class NewsletterSignupView(FormView):
    template_name = 'catalogo/newsletter_signup.html'
    form_class = EmailForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super().form_valid(form)

