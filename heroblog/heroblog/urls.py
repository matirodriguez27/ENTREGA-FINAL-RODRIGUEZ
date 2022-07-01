from django.contrib import admin
from django.urls import path, include
from heroblog.views import inicio


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name = "inicio"),
    path('', include('login.urls')),
]
