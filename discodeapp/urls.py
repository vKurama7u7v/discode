from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name = "index"),
    path('faqs', views.faqs, name = "faqs"),

    path('register', views.register, name = "register"),
    path('login', LoginView.as_view(template_name='registration/login.html'), name = "login"),
    path('logout', LogoutView.as_view(template_name='registration/logout.html'), name = "logout"),
    path('profile', views.miperfil, name = "profile"),
    path('profile/<str:username>', views.perfil, name = "profile"),
    path('follow/<str:username>/', views.follow, name = "follow"),
    path('unfollow/<str:username>/', views.unfollow, name = "unfollow"),
    path('settings', views.settings, name = "settings"),

    path('aprendizaje', views.home, name = "home"),
    path('aprendizaje/<slug:slugcurso>', views.cursoinfo, name = "detalle_curso"),
    path('tema/<slug:slugleccion>', views.leccioninfo, name = "detalle_leccion"),

    path('comunidad', views.feed, name = "feed"),

    path('challenges', views.challenge, name = "challenges"),
    path('challenges/<slug:slug>', views.detalle_challenge, name = "detalle_challenge"),

    path('blog', views.blog, name = "blog"),
    path('blog/categoria/tecnologia', views.tecnologia, name = "TECNOLOGIA"),
    path('blog/categoria/programacion', views.programacion, name = "PROGRAMACION"),
    path('blog/categoria/diseño', views.diseño, name = "DISEÑO"),
    path('blog/categoria/marketing', views.marketing, name = "MARKETING"),
    path('blog/categoria/videojuegos', views.videojuegos, name = "VIDEOJUEGOS"),
    path('blog/categoria/how_to', views.how_to, name = "HOW-TO"),
    path('blog/<slug:slug>', views.detallePost, name = "detalle_post"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)