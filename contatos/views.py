from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.
def index(request):
    contatos = Contato.objects.order_by('nome').filter(mostrar=True)
    paginator = Paginator(contatos, 5)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {'contatos': contatos})

def detalhes(request, id):
    #contato = Contato.objects.get(id=id)
    contato = get_object_or_404(Contato, id=id)
    if not contato.mostrar:
        raise Http404
    return render(request, 'contatos/detalhes.html', {'contato': contato})

def busca(request):
    contatos = Contato.objects.order_by('nome').filter(mostrar=True)
    paginator = Paginator(contatos, 5)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {'contatos': contatos})