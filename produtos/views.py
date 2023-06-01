from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic.list import ListView
# from bar.config import CLOUD_URL
import os
from . import models


def produtos(request, categoria_id=None):
    if categoria_id:
        produtos = models.Produto.objects.filter(categoria=categoria_id)
        categoria_selecionada = models.Categoria.objects.get(id=categoria_id)
    else:
        produtos = models.Produto.objects.all()
        categoria_selecionada = None
    categorias = models.Categoria.objects.all()

    context = {
        'produtos': produtos,
        'categorias': categorias,
        'categoria_selecionada': categoria_selecionada,
        'carrinho': request.session.get('carrinho', {})
    }
    return render(request, 'produtos/produtos.html', context)


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request, 'Você precisa estar logado em uma conta antes de adicionar algum produto.')  # noqa
            return redirect('accounts:renderiza')

        produto_id = self.request.GET.get('pid')
        if not produto_id:
            messages.error(self.request, 'Produto não existe')
            return redirect('produto:produtos')

        produto = get_object_or_404(models.Produto, id=produto_id)
        produto_nome = produto.nome
        imagem = produto.imagem
        categoria = produto.categoria.nome
        preco = produto.preco
        categoria_id = produto.categoria.id
        estoque = produto.estoque

        url = os.getenv('CLOUD_URL')

        if imagem:
            imagem = f'{url}{imagem.name}'

        if produto.estoque or produto.estoque == 0:
            if produto.estoque < 1:
                messages.error(self.request, 'Estoque insuficiente')
                return redirect('produto:produtos')

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']

        if produto_id in carrinho:
            quantidade_carrinho = carrinho[produto_id]['quantidade']
            quantidade_carrinho += 1

            if estoque or estoque == 0:
                if estoque < quantidade_carrinho:
                    messages.warning(
                        self.request, f'Estoque insuficiente para {quantidade_carrinho}x no produto "{produto_nome}". Adicionamos {estoque}x no seu carrinho.')  # noqa
                    quantidade_carrinho = estoque

            carrinho[produto_id]['quantidade'] = quantidade_carrinho
            carrinho[produto_id]['preco_quantitativo'] = preco * \
                quantidade_carrinho

        else:
            carrinho[produto_id] = {
                'produto_id': produto_id,
                'produto_nome': produto_nome,
                'categoria': categoria,
                'preco': preco,
                'preco_quantitativo': preco,
                'imagem': imagem,
                'categoria_id': categoria_id,
                'quantidade': 1,
            }

        self.request.session.save()
        messages.success(
            self.request, f'Produto {produto_nome} adicionado ao seu carrinho {carrinho[produto_id]["quantidade"]}x')  # noqa
        return redirect('produto:produtos')


class RemoverDoCarrinho(ListView):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('accounts:renderiza')

        produto_id = self.request.GET.get('pid')

        if not produto_id:
            return redirect('produto:produtos')

        if not self.request.session.get('carrinho'):
            return redirect('produto:produtos')

        if produto_id not in self.request.session['carrinho']:
            return redirect('produto:produtos')

        carrinho = self.request.session['carrinho'][produto_id]

        messages.success(
            self.request,
            f'Produto {carrinho["produto_nome"]} removido do seu carrinho.'
        )

        del self.request.session['carrinho'][produto_id]
        self.request.session.save()

        return redirect('produto:carrinho')


class RemoverDoCarrinhoUm(ListView):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('accounts:renderiza')
        produto_id = self.request.GET.get('pid')
        if not produto_id:
            return redirect('produto:produtos')

        if not self.request.session.get('carrinho'):
            return redirect('produto:produtos')

        if produto_id not in self.request.session['carrinho']:
            return redirect('produto:produtos')

        carrinho = self.request.session['carrinho']

        quantidade_carrinho = carrinho[produto_id]['quantidade']
        if quantidade_carrinho < 1:
            return redirect('produto:produtos')

        quantidade_carrinho -= 1

        messages.success(
            self.request,
            f'Uma unidade do produto {carrinho[produto_id]["produto_nome"]} removida do seu carrinho.'  # noqa
        )

        if quantidade_carrinho == 0:
            del carrinho[produto_id]
            self.request.session.save()
            return redirect('produto:produtos')

        carrinho[produto_id]['quantidade'] = quantidade_carrinho
        self.request.session.save()

        return redirect('produto:produtos')


class Carrinho(ListView):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('accounts:renderiza')
        context = {'carrinho': self.request.session.get('carrinho', {})}
        return render(self.request, 'produtos/carrinho.html', context)
