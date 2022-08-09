from atexit import register
from django.contrib import admin

from .models import Habitacao, Morador, Contrato

admin.site.register(Habitacao)
admin.site.register(Morador)
admin.site.register(Contrato)
