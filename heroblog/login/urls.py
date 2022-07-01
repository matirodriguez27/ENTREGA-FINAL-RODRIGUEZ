from django.urls import path
from login.views import login_request, signup
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', login_request, name = "login"),
    path('signup', signup, name = "signup"),
    path('logout', LogoutView.as_view(template_name='logout.html'), name = 'logout')
]