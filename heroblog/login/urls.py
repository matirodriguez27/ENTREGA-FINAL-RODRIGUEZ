from django.urls import path
from django.contrib.auth.views import LogoutView
from login import views

urlpatterns = [
    path('login', views.login_request, name = "login"),
    path('signup', views.signup, name = "signup"),
    path('logout', LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    path('profile', views.profile, name = "profile"),
]