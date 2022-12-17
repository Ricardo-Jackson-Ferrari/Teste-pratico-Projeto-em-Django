from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import PersonRegisterForm
from .models import Person

PERSON_LIST_URL = reverse_lazy('person:listing')


class RegisterPersonView(SuccessMessageMixin, CreateView):
    template_name = 'person/register.html'
    form_class = PersonRegisterForm
    success_message = 'Pessoa cadastrada com sucesso!'
    success_url = PERSON_LIST_URL
    extra_context = {'title': 'Cadastro de pessoa'}


class ListPersonView(ListView):
    model = Person
    template_name = 'person/listing.html'
    extra_context = {'title': 'Listagem de pessoas'}
    ordering = ['first_name', 'last_name']
