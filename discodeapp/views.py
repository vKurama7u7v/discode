from django.shortcuts import render, redirect
from .models import Post, Categoria
from discodefaqs.models import Faqs
from discodecurso.models import CategoriaCurso, Curso, Tema, Leccion
from discoderetos.models import Dificultad, CategoriaReto, Challenge
from discodesocial.models import Profile, Publicacion
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    posts = Post.objects.filter(
        estado = True
    )
    return render(request, 'index.html', {'posts':posts})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('home')

    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


###############   FAQS    #################
def faqs(request):
    faqs = Faqs.objects.filter(estado = True)
    return render(request, 'faqs.html', {'faqs':faqs})



###############   CURSOS    #################
@login_required
def home(request):
    cursos = Curso.objects.filter(estado = True)
    return render(request, 'social/home.html', {'curso':cursos})

@login_required
def cursoinfo(request, slugcurso):
    temas = Tema.objects.filter(estado = True)
    lecciones = Leccion.objects.filter(estado = True)
    curso = get_object_or_404(Curso, slug = slugcurso)
    return render(request, 'social/aprendizaje/cursoinfo.html', {'detalle_curso':curso, 'detalle_tema':temas, 'leccion':lecciones})

@login_required
def leccioninfo(request, slugleccion):
    leccion = get_object_or_404(Leccion, slug = slugleccion)
    lecciones = Leccion.objects.filter(estado = True)
    return render(request, 'social/aprendizaje/leccion.html', {'leccion':leccion, 'lecciones':lecciones})



###############   COMUNIDAD   #################
@login_required
def feed(request):
    publicacion = Publicacion.objects.filter(estado = True)

    context = {'publicacion': publicacion}
    return render(request, 'social/discodesocial/feed.html', context)



###############   CHALLENGES   #################
@login_required
def challenge(request):
    retos = Challenge.objects.filter(estado = True)
    return render(request, 'social/challenge.html', {'reto':retos})

@login_required
def detalle_challenge(request, slug):
    reto = get_object_or_404(Challenge, slug = slug)
    return render(request, 'social/challenge/detalle_challenge.html', {'detalle_challenge':reto})



###############   SOCIAL    #################
@login_required
def miperfil(request):
    return render(request, 'social/miperfil.html')



###############   BLOG    #################
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