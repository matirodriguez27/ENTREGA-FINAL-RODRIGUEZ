from django.urls import path
from blog.views import ListaPosts, DetallePost, nuevoPost, EditarPost, BorrarPost

urlpatterns = [
    path('blog/lista/', ListaPosts.as_view(), name='Lista'),
    path('blog/lista/<pk>/', DetallePost.as_view(), name='Detalle'),
    path('blog/nuevo/', nuevoPost, name='Nuevo'),
    path('blog/edicion/<pk>/', EditarPost.as_view(), name='Editar'),
    path('blog/borrar/<pk>/', BorrarPost.as_view(), name='Borrar'),
]