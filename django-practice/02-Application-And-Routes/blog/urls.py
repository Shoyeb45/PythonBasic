from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "blog-home"),
    path('login/', views.login, name = 'blog-login'),
    path('about/', views.about, name = 'blog-about')
]
