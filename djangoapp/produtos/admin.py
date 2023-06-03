from django.contrib import admin
from .models import Categoria, Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'get_preco_formatado']
    list_display_links = ['nome']


admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
