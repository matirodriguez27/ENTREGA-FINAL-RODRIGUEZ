from django.contrib import admin
from django.urls import path, include
from heroblog.views import inicio, about
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name = "inicio"),
    path('about/', about, name = "about"),
    path('', include('login.urls')),
    path('', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
