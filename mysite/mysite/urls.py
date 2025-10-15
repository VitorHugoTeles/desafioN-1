"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.views.generic.base import RedirectView

urlpatterns = [
    path(
        "",  # 1º argumento: a rota (URL vazia, o root)
        RedirectView.as_view(url='/api/usuario', permanent=False),  # 2º argumento: a view
        name='api-root-redirect'  # 3º argumento: o nome da URL (passado para path(), não para as_view())
    ),    
    path("api/", include('usuarios.urls')),
    path("admin/", admin.site.urls)
]
