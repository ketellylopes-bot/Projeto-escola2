from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('projeto/<int:id>/', views.detalhe, name='detalhe'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/cadastrar/', views.categoria_criar, name='categoria_criar'),
    path('categorias/editar/<int:id>/', views.categoria_editar, name='categoria_editar'),
    path('categorias/excluir/<int:id>/', views.categoria_excluir, name='categoria_excluir'),
    path('tags/', views.tags, name='tags'),
    path('tags/cadastrar/', views.tag_criar, name='tag_criar'),
    path('tags/editar/<int:id>/', views.tag_editar, name='tag_editar'),
    path('tags/excluir/<int:id>/', views.tag_excluir, name='tag_excluir'),
]