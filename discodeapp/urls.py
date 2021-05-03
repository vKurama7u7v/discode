from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('login', views.login, name = "login"),
    path('register', views.register, name = "register"),
    path('blog', views.blog, name = "blog"),
    path('blog/categoria/tecnologia', views.tecnologia, name = "TECNOLOGIA"),
    path('blog/categoria/programacion', views.programacion, name = "PROGRAMACION"),
    path('blog/categoria/diseño', views.diseño, name = "DISEÑO"),
    path('blog/categoria/marketing', views.marketing, name = "MARKETING"),
    path('blog/categoria/videojuegos', views.videojuegos, name = "VIDEOJUEGOS"),
    path('blog/categoria/how_to', views.how_to, name = "HOW-TO"),
    path('blog/<slug:slug>', views.detallePost, name = "detalle_post"),
]