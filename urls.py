# loja/urls.py
from urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define a URL raiz
    path('produto/<int:id>/', views.produto_detalhe, name='produto_detalhe'),  # URL de detalhe do produto
]
