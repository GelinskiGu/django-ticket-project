from django.urls import resolve, reverse

from produtos import views

from .test_product_base import ProductTestBase


class ProdutoViewsTest(ProductTestBase):
    def test_produto_home_view_function_is_correct(self):
        view = resolve(reverse('produto:produtos'))
        self.assertIs(view.func, views.produtos)

    def test_produto_produtos_view_function_is_correct(self):
        view = resolve(reverse('produto:produtos_por_categoria',
                               kwargs={'categoria_id': 1}))
        self.assertIs(view.func, views.produtos)

    def test_produto_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('produto:produtos'))
        self.assertEqual(response.status_code, 200)

    def test_produto_home_view_loads_correct_template(self):
        response = self.client.get(reverse('produto:produtos'))
        self.assertTemplateUsed(response, 'produtos/produtos.html')

    def test_produtos_home_template_loads_any_products(self):
        response = self.client.get(reverse('produto:produtos'))
        response_product = response.context['produtos']
        self.assertEqual(response_product.first().nome, 'Product name')

    def test_produtos_home_template_loads_and_shows_products(self):
        response = self.client.get(reverse('produto:produtos'))
        response_product = response.context['produtos']
        content = response.content.decode('utf-8')
        self.assertIn('Product name', content)
        self.assertIn('123', content)
        self.assertIn('Category', content)
        self.assertEqual(len(response_product), 1)
