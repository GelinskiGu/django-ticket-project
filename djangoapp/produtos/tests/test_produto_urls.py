from django.test import TestCase
from django.urls import reverse


class ProdutoURLsTest(TestCase):
    def test_produtos_home_url_is_correct(self):
        home_url = reverse('produto:produtos')
        self.assertEqual(home_url, '/')

    def test_produtos_por_categoria_url_is_correct(self):
        url = reverse('produto:produtos_por_categoria',
                      kwargs={'categoria_id': 1})
        self.assertEqual(url, '/1/')

    def test_adicionar_ao_carrinho_url_is_correct(self):
        url = reverse('produto:adicionaraocarrinho')
        self.assertEqual(url, '/adicionaraocarrinho/')

    def test_remover_do_carrinho_url_is_correct(self):
        url = reverse('produto:removerdocarrinho')
        self.assertEqual(url, '/removerdocarrinho/')

    def test_remover_do_carrinho_um_url_is_correct(self):
        url = reverse('produto:removerdocarrinhoum')
        self.assertEqual(url, '/removerdocarrinhoum/')

    def test_carrinho_url_is_correct(self):
        url = reverse('produto:carrinho')
        self.assertEqual(url, '/carrinho/')
