"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from blog.views import about_view, contact_view, stack_view, careers_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('about/', about_view, name='about'),
    # path('contact/', contact_view, name='about'),
    # path('stack/', stack_view, name='stack'),
    path('', include('blog.urls'), name='blog'),
    path('about/', about_view, name='about'),
    path('stack/', stack_view, name='stack'),
    path('contact/', contact_view, name='contact'),
    path('careers/', careers_view, name='careers'),

]
