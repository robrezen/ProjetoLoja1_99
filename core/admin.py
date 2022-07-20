from django.contrib import admin
from core import models

# Register your models here.
admin.site.register(models.Vendedor)
admin.site.register(models.Venda)
admin.site.register(models.Produto)
admin.site.register(models.Cliente)
admin.site.register(models.Venda_Produto)