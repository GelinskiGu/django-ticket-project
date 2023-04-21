from django.shortcuts import redirect, render, reverse
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from produtos.models import Produto
from .models import Pedido, ItemPedido
from utils import utils


class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('accounts:renderiza')

        return super().dispatch(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(usuario=self.request.user)
        return qs


class SalvarPedido(View):
    def get(self, *args, **kwargs):
        if not self.request.session.get('carrinho'):
            messages.error(
                self.request,
                'Carrinho vazio.'
            )
            return redirect('produto:produtos')

        carrinho = self.request.session.get('carrinho')
        carrinho_produtos_ids = [values for values in carrinho]
        bd_produtos = list(
            Produto.objects.select_related('categoria').filter(
                id__in=carrinho_produtos_ids)
        )
        qtd_total_carrinho = utils.cart_total_qtd(carrinho)
        valor_total_carrinho = utils.cart_totals(carrinho)

        pedido = Pedido(
            usuario=self.request.user,
            qtd_total=qtd_total_carrinho,
            total=valor_total_carrinho,
            status='C',
        )

        pedido.save()

        ItemPedido.objects.bulk_create(
            [
                ItemPedido(
                    pedido=pedido,
                    produto=v['produto_nome'],
                    produto_id=v['produto_id'],
                    preco=v['preco_quantitativo'],
                    quantidade=v['quantidade'],
                    imagem=v['imagem'],
                ) for v in carrinho.values()
            ]
        )

        messages.success(self.request, 'Pedido salvo!')

        del self.request.session['carrinho']

        return redirect('produto:produtos')


class Detalhe(DispatchLoginRequiredMixin, DetailView):
    model = Pedido
    context_object_name = 'pedido'
    template_name = 'pedido/detalhe.html'
    pk_url_kwarg = 'pk'


class Lista(DispatchLoginRequiredMixin, ListView):
    model = Pedido
    context_object_name = 'pedidos'
    template_name = 'pedido/lista.html'
    paginate_by = 10
    ordering = ['status']


class Finalizar(DispatchLoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        pedido_id = self.request.GET.get('ped')
        pedido = Pedido.objects.get(pk=pedido_id)
        pedido.status = 'F'
        pedido.save()
        return redirect('pedido:lista')
