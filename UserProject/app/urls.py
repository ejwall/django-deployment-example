from django.urls import include, path
from app import views

app_name = 'app'

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    ]
