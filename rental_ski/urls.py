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
    path('equipos/<int:equipo_id>/arrendar/', views.arriendar_view, name='arrendar'),
    path('arriendos/',views.vista_arriendos, name='arriendos'),

    ]

