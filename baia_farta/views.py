from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from . models import Habitacao, Morador, Contrato



class HabitacaoListView(ListView):
    model = Habitacao
    template_name: str = "baiafarta/habitacao_list.html"
    context_object_name = "habitacao_list"

class HabitacaoCreateView(CreateView):
    model = Habitacao
    fields = "__all__"
    template_name = "baiafarta/habitacao_create.html"
    success_url = reverse_lazy('habitacao_list')

class MoradorCreateView(CreateView):
    model = Morador
    fields = "__all__"
    template_name = "baiafarta/morador_create.html"

class MoradorDetailView(DetailView):
    pass


class ContratoView(ListView):
    pass

