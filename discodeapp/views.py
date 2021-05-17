from django.shortcuts import render, redirect
from .models import *
from discodefaqs.models import Faqs
from discodecurso.models import CategoriaCurso, Curso, Tema, Leccion
from discoderetos.models import Dificultad, CategoriaReto, Challenge
from discodesocial.models import Profile, Publicacion, Relationship
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import UserRegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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

def contacto(request):
    context = {}
    return render(request, 'contacto.html')


###############   FAQS    #################
def faqs(request):
    faqs = Faqs.objects.filter(estado = True)
    return render(request, 'faqs.html', {'faqs':faqs})



###############   CURSOS    #################
@login_required
def home(request):
    queryset = request.GET.get("buscarcurso")
    cursos = Curso.objects.filter(estado = True)

    #Busqueda
    if queryset:
        cursos = Curso.objects.filter(Q(titulo__icontains = queryset)).distinct()

    context = {'curso':cursos}
    return render(request, 'social/home.html', context)

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
    current_user = get_object_or_404(User, pk = request.user.pk)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit = False)
            publicacion.user = current_user
            publicacion.save()
            messages.success(request, 'Post enviado')
            return redirect('feed')

    else:
        form = PostForm()

    context = {'publicacion': publicacion, 'form': form}
    return render(request, 'social/discodesocial/feed.html', context)

@login_required
def perfil(request, username=None):
    current_user = request.user
    
    if username and username != current_user.username:
        user = User.objects.get(username = username)
        posts = user.posts.all()
    
    else:
        posts = current_user.posts.all()
        user = current_user

    context = {'user':user, 'posts':posts}
    return render(request, 'social/userprofile.html', context)

@login_required
def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username = username)
    to_user_id = to_user
    rel = Relationship(from_user = current_user, to_user = to_user_id)
    rel.save()
    messages.success(request, f'Ahora sigues a {username}')
    return redirect('feed')

@login_required
def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username = username)
    to_user_id = to_user
    rel = Relationship.objects.filter(from_user = current_user.id, to_user = to_user_id).get()
    rel.delete()
    messages.success(request, f'Ya no sigues a {username}')
    return redirect('feed')



###############   CHALLENGES   #################
@login_required
def challenge(request):
    queryset = request.GET.get("buscarchallenge")
    retos = Challenge.objects.filter(estado = True)

    #Busqueda
    if queryset:
        retos = Challenge.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    return render(request, 'social/challenge.html', {'reto':retos})

@login_required
def detalle_challenge(request, slug):
    reto = get_object_or_404(Challenge, slug = slug)
    return render(request, 'social/challenge/detalle_challenge.html', {'detalle_challenge':reto})



###############   SOCIAL    #################
@login_required
def miperfil(request, username=None):
    current_user = request.user
    
    if username and username != current_user.username:
        user = User.objects.get(username = username)
        posts = user.posts.all()
    
    else:
        posts = current_user.posts.all()
        user = current_user

    context = {'user':user, 'posts':posts}
    return render(request, 'social/miperfil.html', context)

@login_required
def settings(request):
    return render(request, 'social/settings.html')



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