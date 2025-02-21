from django.urls import path
from django.views.decorators.cache import cache_page

from .services import block_user
from .views import RegisterView, UsersListView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('register', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('login', LoginView.as_view(template_name='users/login.html', next_page='clients:home'), name='login'),
    path('logout', LogoutView.as_view(next_page='clients:home'), name='logout'),
    path("users/list", cache_page(60)(UsersListView.as_view()), name="users_list"),
    path("block_user/<int:pk>", block_user, name="block_user"),
]