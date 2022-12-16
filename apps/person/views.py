from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import PersonRegisterForm


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'person/register.html'
    form_class = PersonRegisterForm
    success_message = 'Pessoa cadastrada com sucesso!'
    success_url = reverse_lazy('person:listing')
    extra_context = {'title': 'Cadastro de pessoa'}
