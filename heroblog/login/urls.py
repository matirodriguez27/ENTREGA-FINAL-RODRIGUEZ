from django.urls import path
from django.contrib.auth.views import LogoutView
from login import views

urlpatterns = [
    path('accounts/login', views.login_request, name = "login"),
    path('accounts/signup', views.signup, name = "signup"),
    path('accounts/logout', LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    path('accounts/profile', views.profile, name = "profile"),
]