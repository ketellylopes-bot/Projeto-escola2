from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models.deletion import ProtectedError

from .models import Projeto, Categoria, Tag, Noticia
from .forms import CategoriaForm, TagForm

def lista(request):
    projetos = Projeto.objects.all()
    return render(request, 'lista.html', {'projetos': projetos})

def detalhe(request, id):
    projeto = Projeto.objects.get(id=id)
    return render(request, 'detalhe.html', {'projeto': projeto})

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista.html', {'categorias': categorias})

def categoria_criar(request):
    form = CategoriaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria cadastrada com sucesso!')
            return redirect('core:categorias')

    return render(request, 'categorias/formulario.html', {
        'form': form,
        'titulo': 'Cadastrar categoria'
    })

def categoria_editar(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    form = CategoriaForm(request.POST or None, instance=categoria)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso!')
            return redirect('core:categorias')

    return render(request, 'categorias/formulario.html', {
        'form': form,
        'titulo': 'Editar categoria'
    })

def categoria_excluir(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        try:
            categoria.delete()
            messages.success(request, 'Categoria excluída com sucesso!')
        except ProtectedError:
            messages.error(
                request,
                'Não é possível excluir esta categoria, pois existem notícias vinculadas a ela.'
            )

        return redirect('core:categorias')

    return render(request, 'categorias/excluir.html', {
        'categoria': categoria
    })

def tags(request):
    tags = Tag.objects.all()
    return render(request, 'tags/lista.html', {'tags': tags})

def tag_criar(request):
    form = TagForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Tag cadastrada com sucesso!')
            return redirect('core:tags')

    return render(request, 'tags/formulario.html', {
        'form': form,
        'titulo': 'Cadastrar tag'
    })

def tag_editar(request, id):
    tag = get_object_or_404(Tag, id=id)
    form = TagForm(request.POST or None, instance=tag)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Tag atualizada com sucesso!')
            return redirect('core:tags')

    return render(request, 'tags/formulario.html', {
        'form': form,
        'titulo': 'Editar tag'
    })

def tag_excluir(request, id):
    tag = get_object_or_404(Tag, id=id)

    if request.method == 'POST':
        tag.delete()
        messages.success(request, 'Tag excluída com sucesso!')
        return redirect('core:tags')

    return render(request, 'tags/excluir.html', {
        'tag': tag
    })