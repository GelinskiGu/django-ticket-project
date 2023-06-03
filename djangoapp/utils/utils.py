from pedido.models import Pedido


def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')


def cart_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])


def cart_totals(carrinho):
    return sum([item['preco_quantitativo'] for item in carrinho.values()])


def quantidade(carrinho, produto):
    for id, keys in carrinho.items():
        if int(id) == int(produto):
            for key, value in keys.items():
                if key == 'quantidade':
                    return value
    return 0


def pedido_totals(pedidos):
    return sum([pedido.total for pedido in pedidos])
