from django.test import TestCase

from produtos.models import Categoria, Produto


class ProductTestBase(TestCase):
    def setUp(self) -> None:
        self.make_product()
        return super().setUp()

    def make_category(self, name='Category'):
        return Categoria.objects.create(nome=name)

    def make_product(
        self,
        nome='Product name',
        preco=123,
        categoria_data=None
    ):
        if not categoria_data:
            categoria_data = {}
        return Produto.objects.create(
            nome=nome,
            preco=preco,
            categoria=self.make_category(**categoria_data)
        )
