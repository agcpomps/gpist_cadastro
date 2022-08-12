from django.urls import path

from . views import HabitacaoListView, HabitacaoCreateView, MoradorCreateView, ContratoCreateView, SearchResultsView


urlpatterns = [
    path("habitacao/", HabitacaoListView.as_view(), name="habitacao_list"),
    path("habitacao/create", HabitacaoCreateView.as_view(), name="habitacao_create"),
    path("morador/create", MoradorCreateView.as_view(), name='morador_create'),
    path("contrato/create", ContratoCreateView.as_view(), name='contrato_create'),
    path("search/", SearchResultsView.as_view(), name="search_results")
]
