from django.urls import path

from . views import HabitacaoListView, HabitacaoCreateView, MoradorCreateView


urlpatterns = [
    path("habitacao/", HabitacaoListView.as_view(), name="habitacao_list"),
    path("habitacao/create", HabitacaoCreateView.as_view(), name="habitacao_create"),
    path("morador/create", MoradorCreateView.as_view(), name='morador_create')
]
