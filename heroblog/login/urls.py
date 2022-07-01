from django.urls import path
from heroblog.login import views

urlpatterns = [
    path('login', views.login_request, name = "login"),
    path('signup', views.signup, name = "signup"),
]