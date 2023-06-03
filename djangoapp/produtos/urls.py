from django.urls import path

from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.produtos, name="produtos"),
    path('<int:categoria_id>/', views.produtos, name="produtos_por_categoria"),
    path('adicionaraocarrinho/', views.AdicionarAoCarrinho.as_view(),
         name="adicionaraocarrinho"),
    path('removerdocarrinho/', views.RemoverDoCarrinho.as_view(),
         name="removerdocarrinho"),
    path('removerdocarrinhoum/', views.RemoverDoCarrinhoUm.as_view(),
         name="removerdocarrinhoum"),
    path('carrinho/', views.Carrinho.as_view(), name="carrinho"),
]
