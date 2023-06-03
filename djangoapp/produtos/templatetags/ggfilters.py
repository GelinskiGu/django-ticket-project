from django.template import Library
from utils import utils

register = Library()


@register.filter
def formata_preco(val):
    return utils.formata_preco(val)


@register.filter
def get_item(dictionary, key):
    return dictionary.get[key]['quantidade']


@register.filter
def cart_total_qtd(carrinho):
    return utils.cart_total_qtd(carrinho)


@register.filter
def cart_totals(carrinho):
    return utils.cart_totals(carrinho)


@register.filter
def quantidade(carrinho, produto_id):
    return utils.quantidade(carrinho, produto_id)


@register.filter
def pedido_totals(pedidos):
    return utils.pedido_totals(pedidos)
