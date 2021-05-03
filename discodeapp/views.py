from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    posts = Post.objects.filter(
        estado = True
    )
    return render(request, 'index.html', {'posts':posts})

def login(request):
    return render(request, 'registration/login.html')

def register(request):
    return render(request, 'registration/register.html')

def blog(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)

    #Busqueda
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
    
    #Paginacion
    paginator = Paginator(posts, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'blog.html', {'posts':posts})

def detallePost(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'post.html', {'detalle_post':post})

#Filtrado por Categorias (PENDIENTE LAS DEMAS CATEGORIAS):
#NOTA: Agregar tambien en urls.py

def tecnologia(request):
    posts = Post.objects.filter(
        estado = True
    )

    return render(request, 'tecnologia.html', {'posts':posts})

def programacion(request):
    posts = Post.objects.filter(
        estado = True
    )

    return render(request, 'programacion.html', {'posts':posts})

def diseño(request):
    posts = Post.objects.filter(
        estado = True
    )
    
    return render(request, 'diseño.html', {'posts':posts})

def marketing(request):
    posts = Post.objects.filter(
        estado = True
    )

    return render(request, 'marketing.html', {'posts':posts})

def videojuegos(request):
    posts = Post.objects.filter(
        estado = True
    )
    
    return render(request, 'videojuegos.html', {'posts':posts})

def how_to(request):
    posts = Post.objects.filter(
        estado = True
    )
    
    return render(request, 'how-to.html', {'posts':posts})

