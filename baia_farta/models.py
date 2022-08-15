from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Habitacao(models.Model):
    urbanizacao = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    bloco = models.CharField(max_length=1, blank=True, null=True)
    predio = models.CharField(max_length=10)
    andar = models.CharField(max_length=2)
    entrada = models.CharField(max_length=2)
    numero = models.IntegerField()

    def __str__(self) -> str:
        return f"Urbanização do|a {self.urbanizacao}, rua {self.rua}, predio {self.predio} andar nº {self.andar} numero: {self.numero}"

    def get_absolute_url(self):
        return reverse("habitacao_detail", kwargs={"pk": self.pk})
    


class Morador(models.Model):
    nome = models.CharField(max_length=240)
    bi = models.CharField(max_length=15)
    nif = models.CharField(max_length=15)
    numero_de_telefone = models.CharField(max_length=14, null=True, blank=True)
    numero_alternativo = models.CharField(max_length=14, null=True, blank=True)
    data_de_nascimento = models.DateField()
    email = models.EmailField(null=True, blank=True)
    local_de_trabalho = models.CharField(max_length=120, null=True, blank=True)
    funcionario_publico = models.BooleanField(default=False)

    habitacao = models.OneToOneField(
        Habitacao,
        on_delete=models.CASCADE,
        primary_key=True
    )
    
    @property
    def idade(self):
        return int((datetime.now().date() - self.data_de_nascimento.days / 365.25))

    def __str__(self) -> str:
        return self.nome

    def get_absolute_url(self):
        return reverse("morador_detail", kwargs={"pk": self.pk})
    

class Contrato(models.Model):
    numero_contrato = models.CharField(max_length=20)
    class TipoRenda (models.TextChoices):
        RESOLUVEL =  "RES", _("Resoluvel")
        ARRENDAMENTO = "ARR", _("Arrendamento")

    tipo_de_renda = models.CharField(
        max_length=3,
        choices=TipoRenda.choices,
        default=TipoRenda.ARRENDAMENTO
    )
    inicio_de_contrato = models.DateField()
    morador = models.OneToOneField(
        Morador,
        on_delete=models.CASCADE,
        primary_key=True
    )
    habitacao = models.OneToOneField(
        Habitacao,
        on_delete=models.CASCADE,
    )
    def __str__(self) -> str:
        return self.numero_contrato

    def get_absolute_url(self):
        return reverse("contrato_detail", kwargs={"pk": self.pk})
    
    



