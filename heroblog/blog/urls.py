from django.urls import path
from blog.views import ListaPosts, DetallePost, NuevoPost, EditarPost, BorrarPost


urlpatterns = [
    path('blog/', ListaPosts.as_view(), name='Lista'),
    path('blog/pages/', ListaPosts.as_view(), name='Lista'),
    path('blog/pages/<pk>/', DetallePost.as_view(), name='Detalle'),
    path('blog/nuevo/', NuevoPost.as_view(), name='Nuevo'),
    path('blog/edicion/<pk>/', EditarPost.as_view(), name='Editar'),
    path('blog/borrar/<pk>/', BorrarPost.as_view(), name='Borrar'),
]