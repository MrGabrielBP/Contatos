from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome')        #Clicáveis
    list_filter = ('categoria',)
    list_per_page = 10
    search_fields = ('nome', 'sobrenome')
    list_editable = ('telefone', 'mostrar')     #editáveis

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)


