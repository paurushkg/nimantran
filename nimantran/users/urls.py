from django.urls import path
from .views import register, login_user, dashboard_check, logout_user

urlpatterns = [
    path('register', register, name='register'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
]
