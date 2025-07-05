"""
URL configuration for locallibrary project.

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
from django.views.generic import RedirectView #redirect garxa
from django.conf import settings #settings import garne
from django.conf.urls.static import static #static files haru serve garna

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),  # catalog app bata aaune URLS haru include garne
] 

urlpatterns += [
    path('', RedirectView.as_view(url='catalog/')),  # root URL lai catalog app ko homepage ma redirect garne
]

# Static files (CSS, JavaScript, Images) serve garne
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)