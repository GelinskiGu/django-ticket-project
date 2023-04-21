from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('salvarpedido/', views.SalvarPedido.as_view(), name='salvarpedido'),
    path('lista/', views.Lista.as_view(), name='lista'),
    path('detalhe/<int:pk>', views.Detalhe.as_view(), name='detalhe'),
    path('finalizar/', views.Finalizar.as_view(), name='finalizar'),
]
