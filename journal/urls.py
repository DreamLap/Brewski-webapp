"""journal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url, include
<<<<<<< HEAD


urlpatterns = [
    #path('b_journal/', include('b_journal.urls')),
    path('admin/', admin.site.urls),
    #path('home_page/', include('home_page.urls')),
    url(r'^home_page/', include('home_page.urls')),
=======

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('home_page.urls', namespace = "home_page")),
>>>>>>> 64011ffbbf0288e0cafdde3c0d28eafb71021200
]
