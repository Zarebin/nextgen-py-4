from django.urls import path
from . import views as user_views

urlpatterns = [
    path('login', user_views.LoginView.as_view(), name='login'),
    path('register', user_views.RegisterView.as_view(), name='register'),
    path('logout', user_views.LogoutView.as_view(), name='logout'),
    path('status', user_views.StatusView.as_view(), name='status'),
]
