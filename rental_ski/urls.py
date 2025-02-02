"""
URL configuration for m7django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rental_app import views
from django.urls import path 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('registro/',views.registro, name='registro'),
    path('equipos/', views.equipo_list, name='equipo_list'),
    path('equipos/<int:equipo_id>/arrendar/', views.arrendar_view, name='arrendar'),
    path('arriendos/',views.vista_arriendos, name='arriendos'),
    path('mis_arriendos/',views.vista_arriendos, name='mis_arriendos'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),  # Vista personalizada de login
    

# redes sociales
    path("facebook/", views.facebook_redirect, name="facebook_redirect"),
    path("twitter/", views.twitter_redirect, name="twitter_redirect"),
    path("instagram/", views.instagram_redirect, name="instagram_redirect"),
    path("youtube/", views.youtube_redirect, name="youtube_redirect"),
    ]

